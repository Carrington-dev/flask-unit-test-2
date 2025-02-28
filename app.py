from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Hi Carrington, my name is Wonderful"
    })

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")