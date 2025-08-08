from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

app = Flask(__name__)
app.url_map.strict_slashes = False

DB_NAME = "trip_planner.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return {"status": "Trip Planner API is running"}

# -------------------------
# Trips
# -------------------------
@app.route("/api/trips", methods=["GET"])
def get_trips():
    conn = get_db_connection()
    trips = conn.execute("SELECT * FROM trips").fetchall()
    conn.close()
    return jsonify([dict(trip) for trip in trips])

@app.route("/api/trips/<int:trip_id>", methods=["GET"])
def get_trip(trip_id):
    conn = get_db_connection()
    trip = conn.execute("SELECT * FROM trips WHERE id = ?", (trip_id,)).fetchone()
    conn.close()
    if trip:
        return jsonify(dict(trip))
    return jsonify({"error": "Trip not found"}), 404

# -------------------------
# Favorites
# -------------------------
@app.route("/api/favorites", methods=["GET", "POST"])
def favorites():
    conn = get_db_connection()
    if request.method == "GET":
        favorites = conn.execute("SELECT * FROM favorites").fetchall()
        conn.close()
        return jsonify([dict(f) for f in favorites])
    elif request.method == "POST":
        data = request.get_json()
        conn.execute(
            "INSERT INTO favorites (user_id, trip_id) VALUES (?, ?)",
            (data["user_id"], data["trip_id"])
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Favorite added"}), 201

# -------------------------
# Plans
# -------------------------
@app.route("/api/plans", methods=["GET", "POST"])
def plans():
    conn = get_db_connection()
    if request.method == "GET":
        plans = conn.execute("SELECT * FROM plans").fetchall()
        conn.close()
        return jsonify([dict(p) for p in plans])
    elif request.method == "POST":
        data = request.get_json()
        conn.execute(
            "INSERT INTO plans (user_id, title, budget) VALUES (?, ?, ?)",
            (data["user_id"], data["title"], data["budget"])
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Plan created"}), 201

# -------------------------
# Comments (NEW)
# -------------------------
@app.route("/api/comments", methods=["GET", "POST"])
def comments():
    conn = get_db_connection()
    if request.method == "GET":
        comments = conn.execute("SELECT * FROM comments").fetchall()
        conn.close()
        return jsonify([dict(c) for c in comments])
    elif request.method == "POST":
        data = request.get_json()
        conn.execute(
            "INSERT INTO comments (plan_id, user_id, comment) VALUES (?, ?, ?)",
            (data["plan_id"], data["user_id"], data["comment"])
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "Comment added"}), 201

# -------------------------
# Auth (simple placeholder)
# -------------------------
@app.route("/api/auth", methods=["POST"])
def auth():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    ).fetchone()
    conn.close()

    if user:
        return jsonify({"message": "Login successful", "user_id": user["id"]})
    else:
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
