from flask import Flask, request, jsonify, render_template
import psycopg2
import redis

app = Flask(__name__)

db = psycopg2.connect(
    host="db",
    database="visitors",
    user="postgres",
    password="postgres"
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS visitors(
id SERIAL PRIMARY KEY,
visitor_id VARCHAR(50),
name VARCHAR(100),
purpose VARCHAR(200)
)
""")

db.commit()

r = redis.Redis(host="redis", port=6379)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/visits")
def visits():
    count = r.incr("homepage_visits")
    return jsonify({"visits": count})

@app.route("/visitor", methods=["POST"])
def add_visitor():

    data = request.json

    cursor.execute(
        "INSERT INTO visitors(visitor_id,name,purpose) VALUES(%s,%s,%s)",
        (
            data["visitor_id"],
            data["name"],
            data["purpose"]
        )
    )

    db.commit()

    return jsonify({
        "message":"Visitor Added Successfully"
    })

@app.route("/visitor", methods=["GET"])
def get_visitors():

    cursor.execute(
        "SELECT visitor_id,name,purpose FROM visitors"
    )

    rows = cursor.fetchall()

    visitors = []

    for row in rows:
        visitors.append({
            "visitor_id": row[0],
            "name": row[1],
            "purpose": row[2]
        })

    return jsonify(visitors)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
