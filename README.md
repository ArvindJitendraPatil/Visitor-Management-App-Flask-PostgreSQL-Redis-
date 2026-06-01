# Visitor Management System using Flask, PostgreSQL, Redis & Docker Compose

## 📌 Project Overview

This project is a simple Visitor Management System built using:

- Flask (Web Application)
- PostgreSQL (Database)
- Redis (Cache)
- Docker
- Docker Compose

The application allows users to:

- Add visitor details
- View all visitors
- Store visitor data in PostgreSQL
- Track homepage visits using Redis

---

## 🏗️ Architecture

```text
User
  |
  v
Flask Application
  |
  +-------------> PostgreSQL
  |                    |
  |                    +---- Stores Visitor Details
  |
  +-------------> Redis
                       |
                       +---- Homepage Visit Counter
```

---

## 📂 Project Structure

```text
visitor-management-app/
│
├── docker-compose.yml
│
└── web/
    ├── app.py
    ├── requirements.txt
    └── Dockerfile
```

---

## 🚀 Technologies Used

- Python 3.11
- Flask
- PostgreSQL 15
- Redis 7
- Docker
- Docker Compose

---

## 📋 Prerequisites

Install the following:

- Docker
- Docker Compose

Verify Installation:

```bash
docker --version
docker compose version
```

---

## 📝 requirements.txt

```txt
flask
psycopg2-binary
redis
```

---

## 🐳 Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python","app.py"]
```

---

## 📝 app.py

```python
from flask import Flask, request, jsonify
import psycopg2
import redis
import time

app = Flask(__name__)

# PostgreSQL Connection
while True:
    try:
        conn = psycopg2.connect(
            host="postgres",
            database="visitors",
            user="admin",
            password="admin123"
        )

        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS visitors(
            id SERIAL PRIMARY KEY,
            visitor_id VARCHAR(20),
            name VARCHAR(100),
            purpose VARCHAR(100)
        )
        """)

        conn.commit()
        break

    except Exception:
        print("Waiting for PostgreSQL...")
        time.sleep(5)

# Redis Connection
while True:
    try:
        r = redis.Redis(
            host="redis",
            port=6379,
            decode_responses=True
        )

        r.ping()
        break

    except Exception:
        print("Waiting for Redis...")
        time.sleep(5)

@app.route("/")
def home():

    visits = r.incr("homepage_visits")

    return jsonify({
        "message": "Visitor Management System",
        "homepage_visits": visits
    })

@app.route("/visitor", methods=["POST"])
def add_visitor():

    data = request.get_json()

    cur.execute(
        """
        INSERT INTO visitors(visitor_id,name,purpose)
        VALUES(%s,%s,%s)
        """,
        (
            data["visitor_id"],
            data["name"],
            data["purpose"]
        )
    )

    conn.commit()

    return jsonify({
        "message": "Visitor Added Successfully"
    })

@app.route("/visitor", methods=["GET"])
def get_visitors():

    cur.execute(
        """
        SELECT visitor_id,name,purpose
        FROM visitors
        """
    )

    rows = cur.fetchall()

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
```

---

## 🐳 docker-compose.yml

```yaml
services:

  web:
    build: ./web
    container_name: visitor-app

    ports:
      - "5000:5000"

    depends_on:
      - postgres
      - redis

  postgres:
    image: postgres:15

    container_name: postgres-db

    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin123
      POSTGRES_DB: visitors

    ports:
      - "5432:5432"

  redis:
    image: redis:7

    container_name: redis-cache

    ports:
      - "6379:6379"
```

---

# ▶️ Running the Application

## Build and Start Containers

```bash
docker compose up --build -d
```

---

## Check Running Containers

```bash
docker ps
```

Expected Output:

```text
visitor-app
postgres-db
redis-cache
```

---

# 🧪 Testing APIs

## Homepage

```bash
curl http://localhost:5000
```

Response:

```json
{
  "message":"Visitor Management System",
  "homepage_visits":1
}
```

---

## Add Visitor

```bash
curl -X POST http://localhost:5000/visitor \
-H "Content-Type: application/json" \
-d '{
  "visitor_id":"VIS001",
  "name":"Arvind Patil",
  "purpose":"Interview"
}'
```

Response:

```json
{
  "message":"Visitor Added Successfully"
}
```

---

## Get All Visitors

```bash
curl http://localhost:5000/visitor
```

Response:

```json
[
  {
    "visitor_id":"VIS001",
    "name":"Arvind Patil",
    "purpose":"Interview"
  }
]
```

---

# 🔥 Docker Commands Used

Build Image:

```bash
docker compose build
```

Start Containers:

```bash
docker compose up -d
```

Stop Containers:

```bash
docker compose down
```

View Logs:

```bash
docker compose logs -f
```

List Running Containers:

```bash
docker ps
```

---

# 📚 Learning Outcomes

Through this project, I learned:

- Creating Dockerfiles
- Building custom Docker images
- Running multi-container applications
- Using Docker Compose
- Connecting Flask with PostgreSQL
- Using Redis as a cache
- Container networking
- API development using Flask

---

# 👨‍💻 Author

**Arvind Patil**

DevOps Engineer | Docker | Linux | AWS | CI/CD

---

## ⭐ If you found this project useful, don't forget to star the repository.
