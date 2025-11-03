import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Wrap the import in try-catch to get better error messages
try:
    from app import app
    print("✅ Flask app imported successfully")
except Exception as e:
    print(f"❌ ERROR importing app: {e}")
    import traceback
    traceback.print_exc()
    raise

# This is the WSGI entry point for Vercel
app = app  # Keep the same name for Vercel
