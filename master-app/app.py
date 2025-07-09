from flask import Flask, request, jsonify
import redis
import json
from datetime import datetime

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.route('/store-login', methods=['POST'])
def store_login():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"status": "error", "message": "Username missing"}), 400

    login_data = {
        "username": username,
        "timestamp": datetime.utcnow().isoformat(),
        "ip_address": request.remote_addr,
        "user_agent": request.headers.get("User-Agent")
    }

    session_key = f"session:{username}:{datetime.utcnow().timestamp()}"
    r.setex(session_key, 600, json.dumps(login_data))

    return jsonify({"status": "success", "message": "Login session stored"}), 200


@app.route('/session/<username>', methods=['GET'])
def get_session(username):
    keys = r.keys(f"session:{username}:*")
    if not keys:
        return jsonify({"error": "Session not found"}), 404

    latest_key = sorted(keys)[-1]
    session_data = r.get(latest_key)

    if not session_data:
        return jsonify({"error": "Session expired or not found"}), 404

    return jsonify(json.loads(session_data))


if __name__ == "__main__":
    app.run(port=5001)
