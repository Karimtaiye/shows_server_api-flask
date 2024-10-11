from flask import Flask, request, render_template, jsonify
from db import db

app = Flask(__name__)
conn = db.db_connect("shows.db")

cursor = conn.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    q = request.args.get("q")
    shows = cursor.execute("SELECT * FROM shows WHERE title LIKE ? LIMIT 40 ", ("%" + q + "%",))
    # print(shows)
    shows = [dict(row) for row in shows.fetchall()]
    response = {
        "status": 200,
        "message": "Success",
        'result': shows
    }
    return jsonify(response)
    