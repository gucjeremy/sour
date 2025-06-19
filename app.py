
from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
MODEL_NAME = os.getenv("OLLAMA_MODEL", "codellama")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message")
    response = requests.post(OLLAMA_API_URL, json={
        "model": MODEL_NAME,
        "prompt": user_message,
        "stream": False
    })
    result = response.json()
    return jsonify({"reply": result.get("response", "Sorry, I couldn’t process that.")})

if __name__ == "__main__":
    app.run(debug=True)
