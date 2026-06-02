<h1 align="center">🚀 Visitor Management System</h1>

<p align="center">
  <strong>Flask • PostgreSQL • Redis • Docker Compose</strong>
</p>

<p align="center">
  A modern multi-container application demonstrating Docker Networking, Volumes, PostgreSQL, Redis Caching, REST APIs, and a responsive Web UI.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?style=for-the-badge&logo=postgresql">
  <img src="https://img.shields.io/badge/Redis-Cache-red?style=for-the-badge&logo=redis">
  <img src="https://img.shields.io/badge/Docker-Containerization-blue?style=for-the-badge&logo=docker">
  <img src="https://img.shields.io/badge/Docker_Compose-Orchestration-green?style=for-the-badge&logo=docker">
</p>

---

## 📖 Overview

The **Visitor Management System** is a production-style application built with Flask, PostgreSQL, Redis, and Docker Compose.

It demonstrates how multiple services can work together inside containers while maintaining persistence, networking, and scalability.

### ✨ Key Capabilities

- 📝 Add Visitors through a Web UI
- 📋 View Visitor Records instantly
- 🗄️ Store Visitor Information in PostgreSQL
- ⚡ Track Website Visits using Redis
- 🐳 Deploy with Docker Compose
- 💾 Persist Data using Docker Volumes
- 🌐 Enable Container Communication via Docker Networks

---

## 🏗️ Architecture

```text
                    ┌──────────────┐
                    │    User      │
                    └──────┬───────┘
                           │
                           ▼
                ┌────────────────────┐
                │   Flask Web App    │
                │   Visitor UI       │
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

## 🚀 Features

| Feature | Description |
|----------|------------|
| 🌐 Flask Web UI | User-friendly interface |
| 🗄️ PostgreSQL | Persistent visitor storage |
| ⚡ Redis | Homepage visit counter |
| 🐳 Docker Compose | Multi-container deployment |
| 🌐 Docker Network | Container communication |
| 💾 Docker Volumes | Persistent storage |
| 🔌 REST APIs | Add & Retrieve visitors |
| 📱 Responsive UI | HTML, CSS & JavaScript |

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Flask | Web Framework |
| HTML | Frontend Structure |
| CSS | Styling |
| JavaScript | Dynamic Functionality |
| PostgreSQL | Database |
| Redis | Cache |
| Docker | Containerization |
| Docker Compose | Service Orchestration |

---

## 📂 Project Structure

```text
visitor-management-app/
│
├── docker-compose.yml
├── README.md
│
└── web/
    │
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    │
    ├── templates/
    │   └── index.html
    │
    └── static/
        ├── style.css
        └── script.js
```

---

## ⚡ Quick Start

### Build Containers

```bash
docker compose build
```

### Start Application

```bash
docker compose up -d
```

### Verify Containers

```bash
docker ps
```

---

## 🌍 Access Application

Open your browser:

```text
http://<PUBLIC-IP>:5000
```

Example:

```text
http://18.141.186.21:5000
```

---

## 📡 API Endpoints

### Get Homepage

```http
GET /
```

### Add Visitor

```http
POST /visitor
```

Request:

```json
{
  "visitor_id":"VIS001",
  "name":"Arvind Patil",
  "purpose":"Interview"
}
```

Response:

```json
{
  "message":"Visitor Added Successfully"
}
```

---

### Get All Visitors

```http
GET /visitor
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

### Homepage Visit Counter

```http
GET /api/visits
```

Response:

```json
{
  "visits": 10
}
```

---

## 🐳 Docker Components

### Docker Compose Services

| Service | Purpose |
|----------|---------|
| Flask | Web Application |
| PostgreSQL | Visitor Database |
| Redis | Visit Counter Cache |

### Volumes

```text
postgres-data
redis-data
```

### Network

```text
visitor-network
```

---

## 🔍 Verification Commands

### Running Containers

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

## 📸 Screenshots

### 🏠 Home Page

```text
images/homepage.png
```

### ➕ Add Visitor

```text
images/add-visitor.png
```

### 📋 Visitor Records

```text
images/visitor-list.png
```

### 🐳 Running Containers

```text
images/docker-ps.png
```

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in building and deploying a multi-container application using Docker Compose. I learned how to integrate Flask with PostgreSQL and Redis, configure Docker Networks and Volumes, manage container communication, and create a responsive frontend connected to backend APIs.

---

## 👨‍💻 Author

### Arvind Patil

**DevOps Engineer | AWS | Docker | Linux | CI/CD**

📌 Currently building real-world DevOps projects through the **#90DaysOfDevOps** challenge.

---

<p align="center">
⭐ If you found this project useful, consider giving it a Star!
</p>
