from flask import jsonify
from src import app, User

@app.route("/")
def home():
    return jsonify({
        "message": "Hi Carrington, my name is Wonderful"
    })

@app.route("/about")
def about():
    return jsonify({
        "message": "About Us"
    })


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users)  # Dataclass automatically converts to JSON