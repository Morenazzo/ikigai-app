"""
Simple test endpoint to verify Vercel deployment works
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/test')
def test():
    return jsonify({
        "status": "ok",
        "message": "Vercel deployment is working!",
        "python_version": "3.9"
    })

# For Vercel
app = app

