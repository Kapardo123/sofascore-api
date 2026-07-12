from flask import Blueprint, jsonify, request
from sofascore import fetch

teams_bp = Blueprint("teams", __name__)


@teams_bp.route("/search")
def search_teams():
    q = request.args.get("q", "")
    if not q:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    data = fetch("/search/all", {"q": q})
    results = data.get("results", [])
    teams = [r for r in results if r.get("type") == "team"]
    return jsonify({"results": teams})


@teams_bp.route("/<int:team_id>")
def team_info(team_id):
    data = fetch(f"/team/{team_id}")
    return jsonify(data.get("team", data))


@teams_bp.route("/<int:team_id>/image")
def team_image(team_id):
    from flask import Response
    from curl_cffi import requests as cffi_requests
    
    try:
        resp = cffi_requests.get(
            f"https://api.sofascore.com/api/v1/team/{team_id}/image",
            impersonate="chrome131",
            timeout=10
        )
        content_type = resp.headers.get("content-type", "image/png")
        return Response(resp.content, mimetype=content_type,
                       headers={"Cache-Control": "public, max-age=86400"})
    except Exception as e:
        return jsonify({"error": str(e)}), 404


@teams_bp.route("/<int:team_id>/matches/next")
def team_next_matches(team_id):
    page = request.args.get("page", 0, type=int)
    data = fetch(f"/team/{team_id}/events/next/{page}")
    return jsonify({"events": data.get("events", [])})


@teams_bp.route("/<int:team_id>/matches/last")
def team_past_matches(team_id):
    page = request.args.get("page", 0, type=int)
    data = fetch(f"/team/{team_id}/events/last/{page}")
    return jsonify({"events": data.get("events", [])})


@teams_bp.route("/<int:team_id>/transfers")
def team_transfers(team_id):
    data = fetch(f"/team/{team_id}/transfers")
    return jsonify({"transfers": data.get("transfers", data)})


@teams_bp.route("/<int:team_id>/statistics/<int:tournament_id>/<int:season_id>")
def team_statistics(team_id, tournament_id, season_id):
    data = fetch(
        f"/unique-tournament/{tournament_id}/season/{season_id}/team/{team_id}/statistics/overall"
    )
    return jsonify(data)
