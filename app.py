from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)
DATA_FILE = "data/agents.json"

# Page d’accueil = ta carte HTML
@app.route("/")
def index():
    return open("index.html").read()

# API agents (lecture + écriture)
@app.route("/agents", methods=["GET", "POST"])
def agents():
    if request.method == "GET":
        with open(DATA_FILE) as f:
            return jsonify(json.load(f))
    else:
        agents_data = request.json
        with open(DATA_FILE, "w") as f:
            json.dump(agents_data, f)
        return jsonify({"success": True})

# ⬇️ CE BOUT DE CODE EST ESSENTIEL SUR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render fournit le port via la variable PORT
    app.run(host="0.0.0.0", port=port)
