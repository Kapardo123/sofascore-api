from flask import Blueprint, jsonify
from sofascore import fetch
from datetime import date

matches_bp = Blueprint("matches", __name__)


@matches_bp.route("/live")
def live_matches():
    data = fetch("/sport/football/events/live")
    return jsonify({"events": data.get("events", [])})


@matches_bp.route("/date/<date_str>")
def matches_by_date(date_str):
    data = fetch(f"/sport/football/scheduled-events/{date_str}")
    return jsonify({"events": data.get("events", []), "date": date_str})


@matches_bp.route("/today")
def matches_today():
    today = date.today().isoformat()
    data = fetch(f"/sport/football/scheduled-events/{today}")
    return jsonify({"events": data.get("events", []), "date": today})


@matches_bp.route("/<int:event_id>")
def match_details(event_id):
    data = fetch(f"/event/{event_id}")
    return jsonify(data.get("event", data))


@matches_bp.route("/<int:event_id>/incidents")
def match_incidents(event_id):
    data = fetch(f"/event/{event_id}/incidents")
    return jsonify({"incidents": data.get("incidents", [])})


@matches_bp.route("/<int:event_id>/statistics")
def match_statistics(event_id):
    data = fetch(f"/event/{event_id}/statistics")
    return jsonify({"statistics": data.get("statistics", [])})


@matches_bp.route("/<int:event_id>/lineups")
def match_lineups(event_id):
    data = fetch(f"/event/{event_id}/lineups")
    return jsonify(data)


@matches_bp.route("/<int:event_id>/odds")
def match_odds(event_id):
    data = fetch(f"/event/{event_id}/odds/1/all")
    return jsonify(data)


@matches_bp.route("/<int:event_id>/h2h")
def match_h2h(event_id):
    data = fetch(f"/event/{event_id}/h2h")
    return jsonify(data)
