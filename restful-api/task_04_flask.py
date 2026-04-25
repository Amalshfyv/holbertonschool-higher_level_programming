from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return {"error": "User not found"}, 404
    return jsonify(users[username]), 200


@app.post("/add_user")
def add_user():
    data = request.get_json()

    username = data.get("username")
    if username is None:
        return {"error": "Username is required"}, 400

    if username in users:
        return {"error": "User already exists"}, 400

    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    users[username] = user

    return jsonify({
        "message": "User added",
        "user": user
    }), 201


if __name__ == "__main__":
    app.run()