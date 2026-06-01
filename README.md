# 🚀 Visitor Management System

A Dockerized Visitor Management System built using Flask, PostgreSQL, and Redis. This project demonstrates containerized application development, database integration, caching, Docker volumes, Docker networks, and multi-container orchestration using Docker Compose.

---

## 📌 Features

- Add Visitor Details
- View Visitor Details
- Store Visitor Data in PostgreSQL
- Track Homepage Visits using Redis
- Multi-Container Application
- Persistent Data Storage using Docker Volumes
- Custom Docker Network for Container Communication

---

## 🛠️ Tech Stack

- Python 3.11
- Flask
- PostgreSQL
- Redis
- Docker
- Docker Compose

---

## 🏗️ Architecture

```text
                    +------------------+
                    |      User        |
                    +--------+---------+
                             |
                             v
                    +------------------+
                    |   Flask App      |
                    |  (visitor-app)   |
                    +--------+---------+
                             |
              +--------------+--------------+
              |                             |
              v                             v
    +------------------+         +------------------+
    | PostgreSQL DB    |         | Redis Cache      |
    | Stores Visitors  |         | Visitor Counter  |
    +------------------+         +------------------+

Network:
visitor-network

Volumes:
postgres-data
redis-data
```

---

## 📂 Project Structure

```text
visitor-management-app/
│
├── README.md
├── docker-compose.yml
│
└── web/
    ├── app.py
    ├── requirements.txt
    └── Dockerfile
```

---

## 🚀 Setup Instructions

### Clone Repository

```bash
git clone https://github.com/<your-username>/visitor-management-app.git

cd visitor-management-app
```

### Build Containers

```bash
docker compose build
```

### Start Application

```bash
docker compose up -d
```

### Verify Running Containers

```bash
docker ps
```

Expected Containers:

```text
visitor-app
postgres-db
redis-cache
```

---

## 🌐 Access Application

Open Browser:

```text
http://localhost:5000
```

Or:

```bash
curl http://localhost:5000
```

Response:

```json
{
  "message": "Visitor Management System",
  "homepage_visits": 1
}
```

---

## ➕ Add Visitor

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

## 📋 Get All Visitors

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

## 🗄️ Verify PostgreSQL Data

Login to PostgreSQL Container:

```bash
docker exec -it postgres-db psql -U admin -d visitors
```

Check Data:

```sql
SELECT * FROM visitors;
```

Exit:

```sql
\q
```

---

## ⚡ Verify Redis Counter

Login to Redis Container:

```bash
docker exec -it redis-cache redis-cli
```

Check Homepage Counter:

```bash
GET homepage_visits
```

Exit:

```bash
exit
```

---

## 🔗 Verify Docker Network

List Networks:

```bash
docker network ls
```

Inspect Network:

```bash
docker network inspect visitor-management-app_visitor-network
```

---

## 💾 Verify Docker Volumes

List Volumes:

```bash
docker volume ls
```

Expected:

```text
visitor-management-app_postgres-data
visitor-management-app_redis-data
```

Inspect Volume:

```bash
docker volume inspect visitor-management-app_postgres-data
```

---

## 🛑 Stop Application

```bash
docker compose down
```

---

## 🗑️ Remove Containers and Volumes

```bash
docker compose down -v
```

---

## 📚 Docker Concepts Demonstrated

- Dockerfile
- Docker Images
- Docker Containers
- Docker Compose
- Docker Volumes
- Docker Networks
- Flask REST APIs
- PostgreSQL Database Integration
- Redis Cache Integration
- Multi-Container Architecture
- Persistent Storage
- Container Communication

---

## 🎯 Learning Outcomes

Through this project, I learned:

- Building Docker Images
- Running Containers
- Creating Multi-Container Applications
- Using Docker Compose
- Managing Docker Networks
- Managing Docker Volumes
- Connecting Flask with PostgreSQL
- Using Redis for Caching
- Container-to-Container Communication
- Deploying Real-World Applications with Docker

---

## 👨‍💻 Author

**Arvind Patil**

DevOps Engineer | Docker | Linux | AWS | CI/CD

---

⭐ If you found this project useful, consider starring the repository.
