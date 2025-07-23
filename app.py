from flask import Flask, request, render_template, jsonify
from chatbot_logic import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def reply():
    user_input = request.json["msg"]
    return jsonify({"response": get_response(user_input)})

if __name__ == "__main__":
    app.run(debug=True)
