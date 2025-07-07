
from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "data/agents.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/agents", methods=["GET"])
def get_agents():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/api/assign", methods=["POST"])
def assign_agent():
    new_data = request.json
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    data.update(new_data)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    return jsonify(success=True)
