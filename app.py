import os
from dotenv import load_dotenv
import uuid
import json

# Load .env FIRST (before importing other modules)
load_dotenv()

# Use custom SQL wrapper for better serverless compatibility
from db_helper import SQL

from flask import Flask, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from openai import OpenAI

from helpers import apology, login_required
from translations import get_translation, get_user_language, TRANSLATIONS
from clerk_auth import ClerkAuth

# Configure application
app = Flask(__name__)

# Secret key for sessions
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")

# Configure session - use signed cookies for serverless compatibility
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Only initialize Flask-Session if not in serverless environment
# Vercel sets VERCEL_ENV automatically, AWS Lambda sets AWS_LAMBDA_FUNCTION_NAME
if os.getenv("VERCEL_ENV") or os.getenv("AWS_LAMBDA_FUNCTION_NAME"):
    # In serverless, use built-in Flask sessions (signed cookies)
    app.config["SESSION_TYPE"] = None
else:
    # In local development, use filesystem sessions
    Session(app)


# Make translations available in all templates
@app.context_processor
def inject_translations():
    """Make translation function and language available to all templates"""
    lang = session.get('language', 'es')
    return {
        't': lambda key, **kwargs: get_translation(key, lang, **kwargs),
        'lang': lang,
        'translations': TRANSLATIONS.get(lang, TRANSLATIONS['es'])
    }

# Initialize OpenAI client
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key and openai_api_key != "your-openai-api-key-here":
    client = OpenAI(api_key=openai_api_key)
    AI_ENABLED = True
else:
    client = None
    AI_ENABLED = False
    print("⚠️  OpenAI API key not configured. AI features will be disabled.")

# Configure database (use SQLite by default, PostgreSQL if DATABASE_URL is set)
DATABASE_URL = os.getenv("DATABASE_URL")

# In serverless (Vercel/Lambda), prefer /tmp SQLite or PostgreSQL
if (os.getenv("VERCEL_ENV") or os.getenv("AWS_LAMBDA_FUNCTION_NAME")) and not DATABASE_URL:
    # Use /tmp for SQLite in serverless (ephemeral but works)
    DATABASE_URL = "sqlite:////tmp/project.db"
    print("⚠️  Using ephemeral database in serverless environment. Data will be lost on redeploy.")
    print("   For production, configure a PostgreSQL DATABASE_URL.")
elif not DATABASE_URL:
    DATABASE_URL = "sqlite:///project.db"

# Normalize older postgres scheme
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Try to connect to database with fallback to SQLite
try:
    db = SQL(DATABASE_URL)
    print(f"✓ Conectado a base de datos: {DATABASE_URL.split('@')[0] if '@' in DATABASE_URL else 'SQLite'}")
except Exception as e:
    print(f"✗ Error conectando a base de datos: {str(e)}")
    print(f"  Usando SQLite en /tmp como respaldo...")
    DATABASE_URL = "sqlite:////tmp/project.db"
    try:
        db = SQL(DATABASE_URL)
    except Exception as e2:
        print(f"✗ Error crítico: {str(e2)}")
        db = None


def ensure_tables() -> None:
    """Create required tables if they don't exist (works for SQLite and Postgres)."""
    if not db:
        print("⚠️  Database not initialized. Skipping table creation.")
        return
    
    try:
        url = DATABASE_URL.lower() if DATABASE_URL else "sqlite"
        is_sqlite = url.startswith("sqlite")

        if is_sqlite:
            # SQLite DDL
            db.execute(
                """
                CREATE TABLE IF NOT EXISTS ikigai_responses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    love TEXT,
                    needs TEXT,
                    paid TEXT,
                    good TEXT,
                    passion TEXT,
                    mission TEXT,
                    vocation TEXT,
                    profession TEXT,
                    ikigai TEXT,
                    impact TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            db.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    hash TEXT NOT NULL,
                    surfer_points INTEGER DEFAULT 0
                )
                """
            )
            # Add surfer_points column if it doesn't exist (for existing databases)
            try:
                db.execute("ALTER TABLE users ADD COLUMN surfer_points INTEGER DEFAULT 0")
            except:
                pass  # Column already exists
            
            # Add self-evaluation columns for ratings (1-10) and improvement plans
            evaluation_columns = [
                "love_rating INTEGER",
                "love_improvement TEXT",
                "good_rating INTEGER",
                "good_improvement TEXT",
                "paid_rating INTEGER",
                "paid_improvement TEXT",
                "needs_rating INTEGER",
                "needs_improvement TEXT",
                "passion_rating INTEGER",
                "passion_improvement TEXT",
                "mission_rating INTEGER",
                "mission_improvement TEXT",
                "vocation_rating INTEGER",
                "vocation_improvement TEXT",
                "profession_rating INTEGER",
                "profession_improvement TEXT"
            ]
            for column in evaluation_columns:
                try:
                    db.execute(f"ALTER TABLE ikigai_responses ADD COLUMN {column}")
                except:
                    pass  # Column already exists
        else:
            # Postgres DDL
            db.execute(
                """
                CREATE TABLE IF NOT EXISTS ikigai_responses (
                    id SERIAL PRIMARY KEY,
                    love TEXT,
                    needs TEXT,
                    paid TEXT,
                    good TEXT,
                    passion TEXT,
                    mission TEXT,
                    vocation TEXT,
                    profession TEXT,
                    ikigai TEXT,
                    impact TEXT,
                    timestamp TIMESTAMPTZ DEFAULT NOW()
                )
                """
            )
            db.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    hash TEXT NOT NULL,
                    surfer_points INTEGER DEFAULT 0
                )
                """
            )
            # Add surfer_points column if it doesn't exist (for existing databases)
            try:
                db.execute("ALTER TABLE users ADD COLUMN surfer_points INTEGER DEFAULT 0")
            except:
                pass  # Column already exists
            
            # Add self-evaluation columns for ratings (1-10) and improvement plans
            evaluation_columns = [
                "love_rating INTEGER",
                "love_improvement TEXT",
                "good_rating INTEGER",
                "good_improvement TEXT",
                "paid_rating INTEGER",
                "paid_improvement TEXT",
                "needs_rating INTEGER",
                "needs_improvement TEXT",
                "passion_rating INTEGER",
                "passion_improvement TEXT",
                "mission_rating INTEGER",
                "mission_improvement TEXT",
                "vocation_rating INTEGER",
                "vocation_improvement TEXT",
                "profession_rating INTEGER",
                "profession_improvement TEXT"
            ]
            for column in evaluation_columns:
                try:
                    db.execute(f"ALTER TABLE ikigai_responses ADD COLUMN {column}")
                except:
                    pass  # Column already exists
    except Exception as e:
        print(f"⚠️  Error creating tables: {str(e)}")
        print("   The app will still run but database operations may fail.")


# Ensure tables exist on startup
ensure_tables()


@app.before_request
def load_user_points():
    """Load user's surfer points and handle Clerk authentication"""
    # Check for Clerk session token
    clerk_token = (
        request.headers.get("Authorization", "").replace("Bearer ", "") or
        request.cookies.get("__session") or
        request.cookies.get("__clerk_db_jwt")
    )
    
    # If we have a Clerk token and no user_id, authenticate with Clerk
    if clerk_token and not session.get("user_id"):
        clerk = ClerkAuth()
        user_data = clerk.verify_token(clerk_token)
        
        if user_data:
            clerk_user_id = user_data.get("sub")
            email = user_data.get("email", f"clerk_{clerk_user_id}")
            
            # Sync Clerk user to our database
            user_id = clerk.sync_user_to_db(db, clerk_user_id, email)
            if user_id:
                session["user_id"] = user_id
                session["clerk_user_id"] = clerk_user_id
                session["user_email"] = email
    
    # Load surfer points for authenticated user
    user_id = session.get("user_id")
    if user_id:
        try:
            user = db.execute("SELECT surfer_points FROM users WHERE id = ?", user_id)
            if user and len(user) > 0:
                session["total_points"] = user[0]["surfer_points"]
        except Exception as e:
            app.logger.error("Error loading user points: %s", e)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def about():
    """Teach the Ikigai Concept"""
    return render_template("about.html")


@app.route("/auth/clerk-callback", methods=["POST"])
def clerk_callback():
    """Handle Clerk authentication callback"""
    clerk_token = request.form.get('clerk_token')
    email = request.form.get('email')
    lang = request.form.get('lang', 'es')
    
    if clerk_token and email:
        # Verify token with Clerk
        clerk = ClerkAuth()
        user_data = clerk.verify_token(clerk_token)
        
        if user_data:
            # Sync user to database
            clerk_user_id = user_data.get('sub')
            user_id = clerk.sync_user_to_db(db, clerk_user_id, email)
            
            if user_id:
                # Set session
                session['user_id'] = user_id
                session['clerk_user_id'] = clerk_user_id
                session['user_email'] = email
                session['language'] = lang
                
                # Redirect to exercise
                return redirect(f'/exercise?lang={lang}')
    
    # If authentication fails, redirect to landing page
    landing_url = os.getenv("NEXT_PUBLIC_LANDING_URL", "https://ikigai-app-xi.vercel.app")
    return redirect(landing_url)


@app.route("/exercise", methods=["GET", "POST"])
def exercise():
    """Exercise to fill your ikigai - Open access, auth required only to save"""
    # Allow guest access - authentication required only when submitting results
    
    # Create guest session if no user_id
    if not session.get("user_id"):
        # Generate temporary guest ID
        import uuid
        guest_id = f"guest_{uuid.uuid4().hex[:8]}"
        session["guest_id"] = guest_id
        session["is_guest"] = True
    
    # Capture language from URL parameter (e.g., ?lang=es or ?lang=en)
    lang_param = request.args.get('lang')
    if lang_param in ['es', 'en']:
        session['language'] = lang_param
    elif 'language' not in session:
        # Default to Spanish if no language is set
        session['language'] = 'es'
    
    return render_template("exercise.html")

@app.route("/submit_exercise", methods=["POST"])
def submit_exercise():
    import json
    
    # Check if user is authenticated
    if session.get("is_guest") or not session.get("user_id"):
        # Save exercise data to session for after login
        session['pending_exercise_data'] = dict(request.form)
        session['return_to'] = '/save_exercise'
        
        # Redirect to landing page for Clerk authentication
        landing_url = os.getenv("NEXT_PUBLIC_LANDING_URL", "https://ikigai-app-xi.vercel.app")
        return redirect(f"{landing_url}?redirect_to=/save_exercise&auth_required=true")

    # Get JSON data from form
    love = request.form.get("love", "[]")
    good = request.form.get("good", "[]")
    paid = request.form.get("paid", "[]")
    needs = request.form.get("needs", "[]")
    passion = request.form.get("passion", "[]")
    mission = request.form.get("mission", "[]")
    vocation = request.form.get("vocation", "[]")
    profession = request.form.get("profession", "[]")
    ikigai = request.form.get("ikigai", "[]")
    impact = request.form.get("impact", "")
    ikigai_evaluations = request.form.get("ikigai_evaluations", "[]")

    # Convert arrays to comma-separated strings for storage
    try:
        love_list = json.loads(love)
        good_list = json.loads(good)
        paid_list = json.loads(paid)
        needs_list = json.loads(needs)
        passion_list = json.loads(passion)
        mission_list = json.loads(mission)
        vocation_list = json.loads(vocation)
        profession_list = json.loads(profession)
        ikigai_list = json.loads(ikigai)
        
        love_str = ", ".join(love_list) if love_list else ""
        good_str = ", ".join(good_list) if good_list else ""
        paid_str = ", ".join(paid_list) if paid_list else ""
        needs_str = ", ".join(needs_list) if needs_list else ""
        passion_str = ", ".join(passion_list) if passion_list else ""
        mission_str = ", ".join(mission_list) if mission_list else ""
        vocation_str = ", ".join(vocation_list) if vocation_list else ""
        profession_str = ", ".join(profession_list) if profession_list else ""
        ikigai_str = ", ".join(ikigai_list) if ikigai_list else ""
    except:
        love_str = love
        good_str = good
        paid_str = paid
        needs_str = needs
        passion_str = passion
        mission_str = mission
        vocation_str = vocation
        profession_str = profession
        ikigai_str = ikigai

    try:
        # Add columns if they don't exist
        try:
            db.execute("ALTER TABLE ikigai_responses ADD COLUMN impact TEXT")
        except:
            pass  # Column already exists
        
        try:
            db.execute("ALTER TABLE ikigai_responses ADD COLUMN ikigai_evaluations TEXT")
        except:
            pass  # Column already exists
        
        # Insert data
        db.execute(
            "INSERT INTO ikigai_responses (love, needs, paid, good, passion, mission, vocation, ikigai, impact, ikigai_evaluations) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            love_str,
            needs_str,
            paid_str,
            good_str,
            passion_str,
            mission_str,
            vocation_str,
            ikigai_str,
            impact,
            ikigai_evaluations,
        )
        
        # Award Surfer Points! 🏄‍♂️
        # Points breakdown:
        # - 10 points per base section (4 sections: love, good, paid, needs) = 40 points
        # - 15 points per intersection (4 intersections: passion, mission, vocation, profession) = 60 points
        # - 30 points for defining Ikigai keywords = 30 points
        # - 20 points for Impact vision = 20 points
        # - 50 points bonus for completing everything = 50 points
        # Total = 200 points
        
        points_breakdown = {
            'base_sections': 40,  # 10 points each x 4
            'intersections': 60,  # 15 points each x 4
            'ikigai_keywords': 30,
            'impact_vision': 20,
            'completion_bonus': 50
        }
        points_awarded = sum(points_breakdown.values())
        
        user_id = session.get("user_id")
        
        if user_id:
            try:
                db.execute(
                    "UPDATE users SET surfer_points = surfer_points + ? WHERE id = ?",
                    points_awarded,
                    user_id
                )
                session["points_earned"] = points_awarded
                session["points_breakdown"] = points_breakdown
            except Exception as e:
                app.logger.error("Error awarding points: %s", e)
        
    except Exception as e:
        app.logger.error(
            "Error while submitting exercise: %s", e
        )
        return apology("An error occurred. Please try again.")

    return redirect("/results")


@app.route("/save_exercise", methods=["GET"])
@login_required
def save_exercise():
    """Save exercise data after user authenticates via Clerk"""
    # Check if there's pending exercise data
    pending_data = session.get('pending_exercise_data')
    
    if not pending_data:
        # No pending data, redirect to results or exercise
        return redirect("/exercise")
    
    # Clear guest flag
    session.pop('is_guest', None)
    session.pop('guest_id', None)
    
    # Process the saved data (reuse submit_exercise logic)
    import json
    
    love = pending_data.get("love", "[]")
    good = pending_data.get("good", "[]")
    paid = pending_data.get("paid", "[]")
    needs = pending_data.get("needs", "[]")
    passion = pending_data.get("passion", "[]")
    mission = pending_data.get("mission", "[]")
    vocation = pending_data.get("vocation", "[]")
    profession = pending_data.get("profession", "[]")
    ikigai = pending_data.get("ikigai", "[]")
    impact = pending_data.get("impact", "")
    ikigai_evaluations = pending_data.get("ikigai_evaluations", "[]")
    
    # Convert arrays to comma-separated strings for storage
    try:
        love_list = json.loads(love)
        good_list = json.loads(good)
        paid_list = json.loads(paid)
        needs_list = json.loads(needs)
        passion_list = json.loads(passion)
        mission_list = json.loads(mission)
        vocation_list = json.loads(vocation)
        profession_list = json.loads(profession)
        ikigai_list = json.loads(ikigai)
        
        love_str = ", ".join(love_list) if love_list else ""
        good_str = ", ".join(good_list) if good_list else ""
        paid_str = ", ".join(paid_list) if paid_list else ""
        needs_str = ", ".join(needs_list) if needs_list else ""
        passion_str = ", ".join(passion_list) if passion_list else ""
        mission_str = ", ".join(mission_list) if mission_list else ""
        vocation_str = ", ".join(vocation_list) if vocation_list else ""
        profession_str = ", ".join(profession_list) if profession_list else ""
        ikigai_str = ", ".join(ikigai_list) if ikigai_list else ""
    except:
        love_str = love
        good_str = good
        paid_str = paid
        needs_str = needs
        passion_str = passion
        mission_str = mission
        vocation_str = vocation
        profession_str = profession
        ikigai_str = ikigai

    try:
        # Insert data
        db.execute(
            "INSERT INTO ikigai_responses (love, needs, paid, good, passion, mission, vocation, ikigai, impact, ikigai_evaluations) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            love_str,
            needs_str,
            paid_str,
            good_str,
            passion_str,
            mission_str,
            vocation_str,
            ikigai_str,
            impact,
            ikigai_evaluations,
        )
        
        # Award Surfer Points
        points_breakdown = {
            'base_sections': 40,
            'intersections': 60,
            'ikigai_keywords': 30,
            'impact_vision': 20,
            'completion_bonus': 50
        }
        points_awarded = sum(points_breakdown.values())
        
        user_id = session.get("user_id")
        if user_id:
            try:
                db.execute(
                    "UPDATE users SET surfer_points = surfer_points + ? WHERE id = ?",
                    points_awarded,
                    user_id
                )
                session["points_earned"] = points_awarded
                session["points_breakdown"] = points_breakdown
            except Exception as e:
                app.logger.error("Error awarding points: %s", e)
        
        # Clear pending data
        session.pop('pending_exercise_data', None)
        
    except Exception as e:
        app.logger.error("Error saving exercise after auth: %s", e)
        return apology("Error saving your Ikigai. Please try again.")
    
    return redirect("/results")


@app.route("/thanks")
def thanks():
    """Display thank you message after submitting the exercise."""
    return render_template("thanks.html")




@app.route("/results")
def results():
    """Display all stored Ikigai responses."""
    import json
    responses = db.execute(
        "SELECT * FROM ikigai_responses ORDER BY timestamp DESC"
    )
    # Parse ikigai_evaluations JSON into a list for template usage
    for row in responses:
        eval_str = row.get("ikigai_evaluations") if isinstance(row, dict) else None
        parsed = []
        if eval_str:
            try:
                parsed = json.loads(eval_str)
                if not isinstance(parsed, list):
                    parsed = []
            except Exception:
                parsed = []
        row["ikigai_eval_list"] = parsed
    return render_template("results.html", responses=responses)


@app.route("/save_evaluation", methods=["POST"])
def save_evaluation():
    """Save user's self-evaluation ratings and improvement plans"""
    try:
        response_id = request.form.get("response_id")
        if not response_id:
            return jsonify({"success": False, "error": "No response ID provided"}), 400
        
        # Get all ratings and improvements from the form
        updates = []
        values = []
        
        categories = ['love', 'good', 'paid', 'needs', 'passion', 'mission', 'vocation', 'profession']
        
        for category in categories:
            rating = request.form.get(f"{category}_rating")
            improvement = request.form.get(f"{category}_improvement", "").strip()
            
            if rating:
                updates.append(f"{category}_rating = ?")
                values.append(int(rating))
            
            if improvement:
                updates.append(f"{category}_improvement = ?")
                values.append(improvement)
        
        # Update the database
        if updates:
            values.append(response_id)
            query = f"UPDATE ikigai_responses SET {', '.join(updates)} WHERE id = ?"
            db.execute(query, *values)
            
            return jsonify({"success": True, "message": "Evaluación guardada correctamente"})
        else:
            return jsonify({"success": False, "error": "No data to save"}), 400
            
    except Exception as e:
        print(f"Error saving evaluation: {str(e)}")
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/dashboard")
def dashboard():
    """Dashboard with all Ikigai journeys"""
    user_id = session.get("user_id")
    
    # Get all Ikigai responses
    responses = db.execute("SELECT * FROM ikigai_responses ORDER BY timestamp DESC")
    
    # Get user points if logged in
    user_points = 0
    if user_id:
        user_data = db.execute("SELECT surfer_points FROM users WHERE id = ?", user_id)
        if user_data:
            user_points = user_data[0]["surfer_points"]
    
    return render_template("dashboard.html", responses=responses, user_points=user_points)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Redirect to Clerk authentication"""
    # Store where user was trying to go
    return_to = request.args.get('return_to', '/exercise')
    session['return_to'] = return_to
    
    # Redirect to Clerk Account Portal for authentication
    clerk_domain = "https://live-jaybird-81.accounts.dev"
    landing_url = os.getenv("NEXT_PUBLIC_LANDING_URL", "https://ikigai-app-xi.vercel.app")
    
    # Redirect to landing page which will handle Clerk authentication
    return redirect(f"{landing_url}?redirect_to={return_to}")


@app.route("/logout")
def logout():
    """Log user out"""
    # Clear Flask session
    session.clear()
    
    # Redirect to landing page (Clerk will handle logout)
    landing_url = os.getenv("NEXT_PUBLIC_LANDING_URL", "https://ikigai-app-xi.vercel.app")
    return redirect(landing_url)


@app.route("/impact", methods=["GET", "POST"])
def impact():
    """Show how many responses have been submitted."""
    responses = db.execute("SELECT * FROM ikigai_responses ORDER BY timestamp DESC")
    count = len(responses)
    return render_template("impact.html", responses=responses, count=count)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Redirect to Clerk sign up"""
    # Store where user was trying to go
    return_to = request.args.get('return_to', '/exercise')
    session['return_to'] = return_to
    
    # Redirect to landing page for Clerk authentication
    landing_url = os.getenv("NEXT_PUBLIC_LANDING_URL", "https://ikigai-app-xi.vercel.app")
    return redirect(f"{landing_url}?redirect_to={return_to}")




@app.route("/share", methods=["GET", "POST"])
def share():
    """Page to share the stored Ikigai responses."""
    responses = db.execute(
        "SELECT * FROM ikigai_responses ORDER BY timestamp DESC"
    )
    return render_template("share.html", responses=responses)


# ========== AI ENDPOINTS ==========

@app.route("/ai/suggest_intersection", methods=["POST"])
def ai_suggest_intersection():
    """AI suggestions for intersection categories (Passion, Mission, Vocation, Profession)"""
    if not AI_ENABLED:
        return jsonify({"error": "AI features are not enabled. Please configure OPENAI_API_KEY."}), 503
    
    try:
        data = request.get_json()
        category1 = data.get("category1", [])
        category2 = data.get("category2", [])
        intersection_name = data.get("intersection_name", "")
        
        if not category1 or not category2:
            return jsonify({"error": "Missing categories"}), 400
        
        # Create prompt for GPT
        prompt = f"""Analyze these two lists and suggest up to 5 items that could be the intersection between them for someone discovering their {intersection_name}.

List 1: {', '.join(category1)}
List 2: {', '.join(category2)}

Please identify patterns, overlaps, or complementary elements that combine both lists. Provide ONLY a JSON array of strings (maximum 5 suggestions), nothing else. Each suggestion should be 2-5 words max.

Example format: ["suggestion 1", "suggestion 2", "suggestion 3"]"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful career and life purpose coach helping people discover their Ikigai. Be insightful, specific, and concise."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        
        suggestions_text = response.choices[0].message.content.strip()
        
        # Parse JSON response
        try:
            suggestions = json.loads(suggestions_text)
        except:
            # If not valid JSON, try to extract suggestions
            suggestions = [s.strip(' "\'') for s in suggestions_text.strip('[]').split(',')]
            suggestions = [s for s in suggestions if s][:5]
        
        return jsonify({"suggestions": suggestions})
        
    except Exception as e:
        app.logger.error(f"AI suggestion error: {e}")
        return jsonify({"error": "Failed to generate suggestions"}), 500


@app.route("/ai/suggest_ikigai", methods=["POST"])
def ai_suggest_ikigai():
    """AI suggestions for final Ikigai keywords"""
    if not AI_ENABLED:
        return jsonify({"error": "AI features are not enabled. Please configure OPENAI_API_KEY."}), 503
    
    try:
        data = request.get_json()
        passion = data.get("passion", [])
        mission = data.get("mission", [])
        vocation = data.get("vocation", [])
        profession = data.get("profession", [])
        
        prompt = f"""Based on these four key areas, suggest 2-5 powerful keywords that capture this person's Ikigai (their reason for being):

Passion (What they love + What they're good at): {', '.join(passion)}
Mission (What they love + What the world needs): {', '.join(mission)}
Vocation (What the world needs + What they can be paid for): {', '.join(vocation)}
Profession (What they're good at + What they can be paid for): {', '.join(profession)}

Provide ONLY a JSON array of 2-5 powerful, inspiring keywords/short phrases (each 1-3 words max) that synthesize their divine purpose. No explanation.

Example format: ["keyword1", "keyword2", "keyword3"]"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a spiritual life purpose coach helping people crystallize their Ikigai into powerful, memorable keywords. Be profound yet concise."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=150
        )
        
        suggestions_text = response.choices[0].message.content.strip()
        
        try:
            suggestions = json.loads(suggestions_text)
        except:
            suggestions = [s.strip(' "\'') for s in suggestions_text.strip('[]').split(',')]
            suggestions = [s for s in suggestions if s][:5]
        
        return jsonify({"suggestions": suggestions})
        
    except Exception as e:
        app.logger.error(f"AI Ikigai suggestion error: {e}")
        return jsonify({"error": "Failed to generate Ikigai suggestions"}), 500


@app.route("/ai/analyze_results", methods=["POST"])
def ai_analyze_results():
    """AI analysis and advice for completed Ikigai"""
    if not AI_ENABLED:
        return jsonify({"error": "AI features are not enabled. Please configure OPENAI_API_KEY."}), 503
    
    try:
        data = request.get_json()
        ikigai_data = data.get("ikigai_data", {})
        user_question = data.get("question", "")
        
        love = ikigai_data.get("love", "")
        good = ikigai_data.get("good", "")
        paid = ikigai_data.get("paid", "")
        needs = ikigai_data.get("needs", "")
        passion = ikigai_data.get("passion", "")
        mission = ikigai_data.get("mission", "")
        vocation = ikigai_data.get("vocation", "")
        profession = ikigai_data.get("profession", "")
        ikigai = ikigai_data.get("ikigai", "")
        impact = ikigai_data.get("impact", "")
        
        if user_question:
            # User asked a specific question
            prompt = f"""Based on this person's Ikigai discovery, answer their question:

Their Ikigai: {ikigai}
What they love: {love}
What they're good at: {good}
What they can be paid for: {paid}
What the world needs: {needs}
Their impact vision: {impact}

User's question: {user_question}

Provide a thoughtful, actionable response (2-3 paragraphs max) that helps them on their journey."""
        else:
            # General analysis
            prompt = f"""Provide a comprehensive analysis and actionable advice for someone who has discovered their Ikigai:

IKIGAI: {ikigai}

What they love: {love}
What they're good at: {good}
What they can be paid for: {paid}
What the world needs: {needs}

Passion: {passion}
Mission: {mission}
Vocation: {vocation}
Profession: {profession}

Their impact vision: {impact}

Provide:
1. A brief validation of their Ikigai (1 paragraph)
2. Key strengths they should leverage (3-4 bullet points)
3. Potential challenges and how to overcome them (2-3 bullet points)
4. 3 concrete next steps to start living their Ikigai
5. An inspiring closing message

Format in clean markdown with headers."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an experienced life coach and career counselor helping people live their Ikigai. Be encouraging, specific, and actionable. Use markdown formatting."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        analysis = response.choices[0].message.content.strip()
        
        return jsonify({"analysis": analysis, "success": True})
        
    except Exception as e:
        app.logger.error(f"AI analysis error: {e}")
        return jsonify({"error": "Failed to generate analysis"}), 500


@app.route("/api/add_points", methods=["POST"])
@login_required
def add_points():
    """Award Surfer Points to user"""
    try:
        data = request.get_json()
        points = int(data.get("points", 0))
        
        if points <= 0 or points > 100:
            return jsonify({"error": "Invalid points amount"}), 400
        
        # Get current points
        user = db.execute("SELECT surfer_points FROM users WHERE id = ?", session["user_id"])
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        current_points = user[0]["surfer_points"] or 0
        new_total = current_points + points
        
        # Update points in database
        db.execute(
            "UPDATE users SET surfer_points = ? WHERE id = ?",
            new_total, session["user_id"]
        )
        
        return jsonify({
            "success": True,
            "points_awarded": points,
            "total_points": new_total
        })
        
    except Exception as e:
        app.logger.error(f"Add points error: {e}")
        return jsonify({"error": "Failed to add points"}), 500


@app.route("/api/get_points", methods=["GET"])
@login_required
def get_points():
    """Get user's current Surfer Points"""
    try:
        user = db.execute("SELECT surfer_points FROM users WHERE id = ?", session["user_id"])
        if not user:
            return jsonify({"error": "User not found"}), 404
        
        points = user[0]["surfer_points"] or 0
        return jsonify({"points": points, "success": True})
        
    except Exception as e:
        app.logger.error(f"Get points error: {e}")
        return jsonify({"error": "Failed to get points"}), 500
