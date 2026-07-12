from flask import Blueprint, jsonify
from sofascore import fetch

tournaments_bp = Blueprint("tournaments", __name__)


@tournaments_bp.route("/categories")
def categories():
    data = fetch("/sport/football/categories")
    return jsonify({"categories": data.get("categories", [])})


@tournaments_bp.route("/categories/<int:category_id>/tournaments")
def category_tournaments(category_id):
    data = fetch(f"/sport/football/categories/{category_id}/unique-tournaments")
    return jsonify({"uniqueTournaments": data.get("uniqueTournaments", [])})


@tournaments_bp.route("/tournaments")
def all_tournaments():
    data = fetch("/config/default-unique-tournaments/PL/football")
    return jsonify({"uniqueTournaments": data.get("uniqueTournaments", [])})


@tournaments_bp.route("/tournaments/<int:tournament_id>")
def tournament_info(tournament_id):
    data = fetch(f"/unique-tournament/{tournament_id}")
    return jsonify(data.get("uniqueTournament", data))


@tournaments_bp.route("/tournaments/<int:tournament_id>/seasons")
def tournament_seasons(tournament_id):
    data = fetch(f"/unique-tournament/{tournament_id}/seasons")
    return jsonify({"seasons": data.get("seasons", [])})


@tournaments_bp.route("/tournaments/<int:tournament_id>/season/<int:season_id>/standings")
def tournament_standings(tournament_id, season_id):
    data = fetch(f"/unique-tournament/{tournament_id}/season/{season_id}/standings/total")
    return jsonify({"standings": data.get("standings", [])})


@tournaments_bp.route("/tournaments/<int:tournament_id>/season/<int:season_id>/top-players")
def tournament_top_players(tournament_id, season_id):
    data = fetch(f"/unique-tournament/{tournament_id}/season/{season_id}/top-players/overall")
    return jsonify(data)


@tournaments_bp.route("/tournaments/<int:tournament_id>/season/<int:season_id>/events/last/<int:page>")
def tournament_events_last(tournament_id, season_id, page):
    data = fetch(f"/unique-tournament/{tournament_id}/season/{season_id}/events/last/{page}")
    return jsonify({"events": data.get("events", []), "hasNextPage": data.get("hasNextPage", False)})


@tournaments_bp.route("/tournaments/<int:tournament_id>/season/<int:season_id>/events/next/<int:page>")
def tournament_events_next(tournament_id, season_id, page):
    data = fetch(f"/unique-tournament/{tournament_id}/season/{season_id}/events/next/{page}")
    return jsonify({"events": data.get("events", []), "hasNextPage": data.get("hasNextPage", False)})
