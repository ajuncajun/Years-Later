# routes/comments.py
from flask import Blueprint, request, jsonify
from db import get_db_connection

comments_bp = Blueprint("comments", __name__)

@comments_bp.route("/<int:plan_id>", methods=["POST"])
def add_comment(plan_id):
    data = request.get_json()
    user_id = data.get("user_id")
    content = data.get("content")

    conn = get_db_connection()
    conn.execute("INSERT INTO comments (plan_id, user_id, content) VALUES (?, ?, ?)",
                 (plan_id, user_id, content))
    conn.commit()
    conn.close()
    return jsonify({"message": "Comment added"}), 201

@comments_bp.route("/<int:plan_id>", methods=["GET"])
def get_comments(plan_id):
    conn = get_db_connection()
    comments = conn.execute("SELECT * FROM comments WHERE plan_id = ?", (plan_id,)).fetchall()
    conn.close()
    return jsonify([dict(c) for c in comments])
