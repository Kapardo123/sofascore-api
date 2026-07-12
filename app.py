from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import os

from routes.matches import matches_bp
from routes.tournaments import tournaments_bp
from routes.teams import teams_bp

load_dotenv()

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("API_KEY", "moj-testowy-klucz")
VALID_KEYS = [k.strip() for k in API_KEY.split(",")]

@app.before_request
def check_auth():
    if request.path == "/test" or request.path.startswith("/static") or "/image" in request.path:
        return None
    api_key = (
        request.headers.get("X-RapidAPI-Proxy-Secret")
        or request.headers.get("X-RapidAPI-Key")
        or request.headers.get("X-API-Key")
        or request.headers.get("Authorization", "").replace("Bearer ", "")
    )
    if not api_key:
        return jsonify({"error": "Missing API key"}), 401
    if api_key not in VALID_KEYS:
        return jsonify({"error": "Invalid API key"}), 403

@app.route("/")
def index():
    return jsonify({
        "name": "Sofascore Scraper API",
        "version": "2.0.0",
        "endpoints": {
            "tournaments": "/api/tournaments",
            "matches": "/api/matches",
            "teams": "/api/teams",
        }
    })

app.register_blueprint(matches_bp, url_prefix="/api/matches")
app.register_blueprint(tournaments_bp, url_prefix="/api/tournaments")
app.register_blueprint(teams_bp, url_prefix="/api/teams")

@app.route("/test")
def dashboard():
    return send_from_directory("static", "dashboard.html")

@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)
