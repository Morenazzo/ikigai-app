from app import app as flask_app

# Vercel expects a top-level WSGI callable named `app` or `handler`.
# Expose both to be safe across builder versions.
app = flask_app
handler = flask_app
