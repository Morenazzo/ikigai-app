#!/usr/bin/env python3
"""Quick test to verify surfer points are working"""

from db_helper import SQL
import os
from dotenv import load_dotenv

load_dotenv()

# Connect to local database
db = SQL("sqlite:///project.db")

# Check if surfer_points column exists
try:
    result = db.execute("SELECT surfer_points FROM users LIMIT 1")
    print("✅ surfer_points column exists in database")
    print(f"   Sample data: {result}")
except Exception as e:
    print(f"❌ Error: {e}")
    
# Check if audio files exist
import os.path
audio_files = ['static/wave-point.mp3', 'static/surf-celebration.mp3']
for audio in audio_files:
    if os.path.exists(audio):
        size = os.path.getsize(audio)
        print(f"✅ {audio} exists ({size} bytes)")
    else:
        print(f"❌ {audio} NOT FOUND")

print("\n🎯 To test live:")
print("1. Run: python app.py")
print("2. Go to: http://localhost:5000/exercise")
print("3. Complete a step and listen for wave sound")
