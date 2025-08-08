# routes/favorites.py
from flask import Blueprint, request, jsonify
from db import get_db_connection

favorites_bp = Blueprint("favorites", __name__)

@favorites_bp.route("/", methods=["POST"])
def add_favorite():
    data = request.get_json()
    user_id = data.get("user_id")
    item_type = data.get("item_type")
    item_id = data.get("item_id")

    conn = get_db_connection()
    conn.execute("INSERT INTO favorites (user_id, item_type, item_id) VALUES (?, ?, ?)",
                 (user_id, item_type, item_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Favorite added"}), 201

@favorites_bp.route("/<int:user_id>", methods=["GET"])
def get_favorites(user_id):
    conn = get_db_connection()
    favs = conn.execute("SELECT * FROM favorites WHERE user_id = ?", (user_id,)).fetchall()
    conn.close()
    return jsonify([dict(f) for f in favs])
