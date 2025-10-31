import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# This is the WSGI entry point for Vercel
application = app

# For compatibility
handler = app
