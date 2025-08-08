# routes/plans.py
from flask import Blueprint, request, jsonify
from db import get_db_connection

plans_bp = Blueprint("plans", __name__)

@plans_bp.route("/", methods=["POST"])
def create_plan():
    data = request.get_json()
    owner_id = data.get("owner_id")
    title = data.get("title")
    destination = data.get("destination")

    if not all([owner_id, title]):
        return jsonify({"error": "Missing fields"}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO plans (owner_id, title, destination) VALUES (?, ?, ?)",
                (owner_id, title, destination))
    conn.commit()
    plan_id = cur.lastrowid
    conn.close()
    return jsonify({"message": "Plan created", "plan_id": plan_id}), 201

@plans_bp.route("/<int:plan_id>", methods=["GET"])
def get_plan(plan_id):
    conn = get_db_connection()
    plan = conn.execute("SELECT * FROM plans WHERE id = ?", (plan_id,)).fetchone()
    items = conn.execute("SELECT * FROM plan_items WHERE plan_id = ?", (plan_id,)).fetchall()
    conn.close()

    if plan:
        return jsonify({
            "plan": dict(plan),
            "items": [dict(item) for item in items]
        })
    return jsonify({"error": "Plan not found"}), 404

@plans_bp.route("/<int:plan_id>/items", methods=["POST"])
def add_plan_item(plan_id):
    data = request.get_json()
    title = data.get("title")
    price = data.get("price", 0)
    created_by = data.get("created_by")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO plan_items (plan_id, title, price, created_by)
                   VALUES (?, ?, ?, ?)""", (plan_id, title, price, created_by))
    conn.commit()
    conn.close()
    return jsonify({"message": "Item added"}), 201
