# user related
import sqlite3
from flask import Blueprint, request, jsonify

user_bp = Blueprint("users", __name__, url_prefix='/api/v1/users')

# function to get db connection
def get_db_connection():
    conn = sqlite3.connect('______.db')
    conn.row_factory = sqlite3.Row
    return conn
@user_bp.route('/', methods=['GET'])
def get_users():
    """Get users (with optional filters)"""
    username = request.args.get('username')
    user_type = request.args.get('type')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM usersTab where 1=1"
    params = []

    if username:
        query += " AND username LIKE"
        params.append(F'%{username}%')
    if user_type:
        query += " AND type LIKE ?"
        params.append(f'%{user_type}%')

    cursor.execute(query, params)
    users = cursor.fetchall()
    conn.close()

    return jsonify([dict(user) for user in users]), 200

@user_bp.route('/', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()

    required_fields = {'username', 'password', 'type'}
    if not data or not required_fields.issubset(data):
        return jsonify({'error': 'Missing required fields'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO usersTab (username, password, type) VALUES (?, ?, ?)",
            (data['username'], data['password'], data['type'])
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({'error': 'Username already exists'}), 400

    conn.close()
    return jsonify({'message': 'User created'}), 201

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete user by ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usersTab WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': f'User with id {user_id} deleted'}), 200
