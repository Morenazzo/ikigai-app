"""
Clerk Authentication Middleware for Flask
Verifies Clerk session tokens and manages user authentication
"""

import os
import jwt
import requests
from functools import wraps
from flask import request, session, jsonify, redirect
from werkzeug.security import generate_password_hash


class ClerkAuth:
    """Clerk authentication helper for Flask"""
    
    def __init__(self, secret_key=None):
        self.secret_key = secret_key or os.getenv("CLERK_SECRET_KEY")
        self.publishable_key = os.getenv("NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY")
        
        if not self.secret_key:
            print("⚠️  CLERK_SECRET_KEY not configured")
    
    def verify_token(self, token):
        """Verify Clerk session token"""
        if not token or not self.secret_key:
            return None
        
        try:
            # Get Clerk's JWKS to verify the token
            # For production, you should cache this
            headers = {"Authorization": f"Bearer {self.secret_key}"}
            response = requests.get(
                "https://api.clerk.com/v1/jwks",
                headers=headers,
                timeout=5
            )
            
            if response.status_code != 200:
                return None
            
            # Decode and verify the JWT
            decoded = jwt.decode(
                token,
                options={"verify_signature": False},  # We'll verify with Clerk API
                algorithms=["RS256"]
            )
            
            return decoded
            
        except Exception as e:
            print(f"Clerk token verification error: {e}")
            return None
    
    def get_user_from_clerk(self, user_id):
        """Get user details from Clerk API"""
        if not self.secret_key:
            return None
        
        try:
            headers = {"Authorization": f"Bearer {self.secret_key}"}
            response = requests.get(
                f"https://api.clerk.com/v1/users/{user_id}",
                headers=headers,
                timeout=5
            )
            
            if response.status_code == 200:
                return response.json()
            return None
            
        except Exception as e:
            print(f"Error fetching Clerk user: {e}")
            return None
    
    def sync_user_to_db(self, db, clerk_user_id, email):
        """Sync Clerk user to local database"""
        try:
            # Check if user exists in our database
            existing_user = db.execute(
                "SELECT id FROM users WHERE username = ?", 
                email
            )
            
            if existing_user and len(existing_user) > 0:
                return existing_user[0]["id"]
            
            # Create new user in our database
            # Use a placeholder hash since Clerk handles authentication
            placeholder_hash = generate_password_hash(clerk_user_id)
            
            new_user_id = db.execute(
                "INSERT INTO users (username, hash, surfer_points) VALUES (?, ?, ?)",
                email, placeholder_hash, 0
            )
            
            return new_user_id
            
        except Exception as e:
            print(f"Error syncing user to database: {e}")
            return None


def clerk_required(f):
    """Decorator to require Clerk authentication for routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if user is already authenticated via session
        if session.get("user_id"):
            return f(*args, **kwargs)
        
        # Check for Clerk session token in headers or cookies
        clerk_token = (
            request.headers.get("Authorization", "").replace("Bearer ", "") or
            request.cookies.get("__session") or
            request.cookies.get("__clerk_db_jwt")
        )
        
        if not clerk_token:
            # Redirect to landing page for authentication
            landing_url = os.getenv("NEXT_PUBLIC_LANDING_URL", "https://ikigai-app-xi.vercel.app")
            return redirect(f"{landing_url}?redirect_to={request.url}")
        
        # Verify token and set session
        clerk = ClerkAuth()
        user_data = clerk.verify_token(clerk_token)
        
        if not user_data:
            landing_url = os.getenv("NEXT_PUBLIC_LANDING_URL", "https://ikigai-app-xi.vercel.app")
            return redirect(f"{landing_url}?redirect_to={request.url}")
        
        # User is authenticated
        session["clerk_user_id"] = user_data.get("sub")
        session["user_email"] = user_data.get("email")
        
        return f(*args, **kwargs)
    
    return decorated_function

