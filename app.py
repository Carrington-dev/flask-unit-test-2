from src import app, db

if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True, port=8000, host="0.0.0.0")