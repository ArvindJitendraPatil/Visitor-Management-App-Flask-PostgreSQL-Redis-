<h1 align="center">🚀 Visitor Management System</h1>

<p align="center">
  <b>Flask + PostgreSQL + Redis + Docker Compose</b>
</p>

<p align="center">
  A production-style multi-container application demonstrating Docker, Networking, Volumes, Databases, Caching, and REST APIs.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Redis-Cache-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Docker-Containerization-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Docker_Compose-Orchestration-green?style=for-the-badge">
</p>

---

# 🌟 Project Overview

This project is a complete Visitor Management System built using modern DevOps practices.

The application allows users to:

✅ Add Visitors

✅ View Visitors

✅ Store Visitor Information in PostgreSQL

✅ Track Website Visits using Redis

✅ Run Multiple Containers using Docker Compose

✅ Persist Data using Docker Volumes

✅ Enable Container Communication using Docker Networks

---

# 🏗️ Solution Architecture

```text
                    ┌──────────────┐
                    │    User      │
                    └──────┬───────┘
                           │
                           ▼
                ┌────────────────────┐
                │   Flask Web App    │
                │   visitor-app      │
                └─────────┬──────────┘
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼

 ┌─────────────────┐           ┌─────────────────┐
 │ PostgreSQL DB   │           │ Redis Cache     │
 │ Visitor Records │           │ Visit Counter   │
 └─────────────────┘           └─────────────────┘

         Docker Network : visitor-network

         Docker Volumes :
         ├── postgres-data
         └── redis-data
```

---

# 🚀 Features

| Feature | Description |
|----------|------------|
| Flask REST API | Handles Requests |
| PostgreSQL | Persistent Visitor Storage |
| Redis | Homepage Visitor Counter |
| Docker Compose | Multi-Container Deployment |
| Docker Network | Container Communication |
| Docker Volumes | Persistent Storage |
| REST APIs | Add and Retrieve Visitors |

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Language |
| Flask | Web Framework |
| PostgreSQL | Database |
| Redis | Cache |
| Docker | Containerization |
| Docker Compose | Orchestration |

---

# 📂 Project Structure

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

# ⚡ Quick Start

### Clone Repository

```bash
git clone https://github.com/<your-username>/visitor-management-app.git
cd visitor-management-app
```

### Build Application

```bash
docker compose build
```

### Run Application

```bash
docker compose up -d
```

### Verify

```bash
docker ps
```

---

# 📡 API Endpoints

## Homepage

```http
GET /
```

Response

```json
{
  "message":"Visitor Management System",
  "homepage_visits":1
}
```

---

## Add Visitor

```http
POST /visitor
```

Request

```json
{
  "visitor_id":"VIS001",
  "name":"Arvind Patil",
  "purpose":"Interview"
}
```

Response

```json
{
  "message":"Visitor Added Successfully"
}
```

---

## Get Visitors

```http
GET /visitor
```

Response

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

# 🐳 Docker Components Used

### Dockerfile

Creates a custom Flask image.

### Docker Compose

Deploys:

- Flask Container
- PostgreSQL Container
- Redis Container

### Docker Volumes

```text
postgres-data
redis-data
```

Used for persistent storage.

### Docker Network

```text
visitor-network
```

Used for secure container communication.

---

# 🔍 Verification Commands

### Containers

```bash
docker ps
```

### Networks

```bash
docker network ls
```

### Volumes

```bash
docker volume ls
```

### Logs

```bash
docker compose logs -f
```

---

# 🎯 Learning Outcomes

By building this project I learned:

✅ Docker Images

✅ Docker Containers

✅ Docker Networking

✅ Docker Volumes

✅ Docker Compose

✅ Flask API Development

✅ PostgreSQL Integration

✅ Redis Integration

✅ Container Communication

✅ Multi-Container Application Deployment

---

# 👨‍💻 Author

### Arvind Patil

DevOps Engineer | AWS | Docker | Linux | CI/CD

📌 Currently learning and building real-world DevOps projects through the #90DaysOfDevOps challenge.

---

## ⭐ Star this repository if you found it useful!
