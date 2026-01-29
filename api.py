from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "todos.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(load_data())

@app.route("/todos", methods=["POST"])
def save_todos():
    data = request.json
    save_data(data)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run()
