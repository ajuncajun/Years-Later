# routes/trips.py
from flask import Blueprint, request, jsonify
from db import get_db_connection

trips_bp = Blueprint("trips", __name__)

@trips_bp.route("/", methods=["GET"])
def list_trips():
    conn = get_db_connection()
    trips = conn.execute("SELECT * FROM trips").fetchall()
    conn.close()
    return jsonify([dict(trip) for trip in trips])

@trips_bp.route("/<int:trip_id>", methods=["GET"])
def trip_detail(trip_id):
    conn = get_db_connection()
    trip = conn.execute("SELECT * FROM trips WHERE id = ?", (trip_id,)).fetchone()
    conn.close()
    if trip:
        return jsonify(dict(trip))
    return jsonify({"error": "Trip not found"}), 404
