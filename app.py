import os
from dotenv import load_dotenv
import uuid
import json

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from openai import OpenAI

from helpers import apology, login_required

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

# Load .env (Neon credentials and OpenAI key)
load_dotenv()

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
    except Exception as e:
        print(f"⚠️  Error creating tables: {str(e)}")
        print("   The app will still run but database operations may fail.")


# Ensure tables exist on startup
ensure_tables()


@app.before_request
def load_user_points():
    """Load user's surfer points into session before each request"""
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


@app.route("/exercise", methods=["GET", "POST"])
def exercise():
    """Exercise to fill you ikigai"""
    return render_template("exercise.html")

@app.route("/submit_exercise", methods=["POST"])
def submit_exercise():
    import json

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
        # Add impact column if it doesn't exist
        try:
            db.execute("ALTER TABLE ikigai_responses ADD COLUMN impact TEXT")
        except:
            pass  # Column already exists
        
        # Insert data
        db.execute(
            "INSERT INTO ikigai_responses (love, needs, paid, good, passion, mission, vocation, ikigai, impact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            love_str,
            needs_str,
            paid_str,
            good_str,
            passion_str,
            mission_str,
            vocation_str,
            ikigai_str,
            impact,
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


@app.route("/thanks")
def thanks():
    """Display thank you message after submitting the exercise."""
    return render_template("thanks.html")




@app.route("/results")
def results():
    """Display all stored Ikigai responses."""
    responses = db.execute(
        "SELECT * FROM ikigai_responses ORDER BY timestamp DESC"
    )
    return render_template("results.html", responses=responses)


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
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/impact", methods=["GET", "POST"])
def impact():
    """Show how many responses have been submitted."""
    responses = db.execute("SELECT * FROM ikigai_responses ORDER BY timestamp DESC")
    count = len(responses)
    return render_template("impact.html", responses=responses, count=count)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if not email or not password or not confirm:
            return apology("No empty Fields")

        if len(password) < 8:
            return apology("Password must be at least 8 characters")

        if password != confirm:
            return apology("Passwords Do Not Match")

        hash = generate_password_hash(password)

        try:
            newUser = db.execute ("INSERT INTO users(username, hash) VALUES (?, ?)", email, hash)
        except:
            return apology("User Already Used")

        session["user_id"] = newUser

        return redirect("/")




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
