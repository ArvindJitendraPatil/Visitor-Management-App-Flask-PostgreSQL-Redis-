# Day 34 – Docker Compose: Real-World Multi-Container Apps

## Task 1: Build Your Own App Stack

### I built a Visitor Management System using:

* A Flask web application for managing visitors
* A PostgreSQL database for storing visitor records
* A Redis cache for tracking homepage visit counts
* Docker Compose for multi-container orchestration
* Docker Volumes for persistent storage
* Docker Networks for container communication

---

## Task 2: depends_on & Healthchecks

* Added PostgreSQL health checks.
* Configured `depends_on` with `condition: service_healthy`.
* Flask application waits until PostgreSQL becomes healthy before starting.

### Result

✅ Application starts only after database is ready.

---

## Task 3: Restart Policies

### Added restart policy

```yaml
restart: always
```

### Test

1. Manually killed PostgreSQL container

```bash
docker kill visitor-management-app-db-1
```

2. Verified container status

```bash
docker ps
```

### Observation

* PostgreSQL container automatically restarted.

### Tested `restart: on-failure`

* Container restarts only when it exits with a failure code.
* Does not restart when manually stopped.

### Notes

#### restart: always

Used for:

* Databases
* Backend APIs
* Production Applications
* Critical Services

#### restart: on-failure

Used for:

* Migration Jobs
* Batch Processing
* One-time Scripts
* Retry-based Workloads

---

## Task 4: Custom Dockerfiles in Compose

### Implemented Custom Build

Instead of pulling a pre-built image, the Flask application is built using:

```yaml
build: ./web
```

### Changes Made

* Modified Flask application code.
* Rebuilt containers.

### Rebuild and Restart

```bash
docker compose up --build -d
```

### Result

✅ Application rebuilt and deployed successfully.

---

## Task 5: Named Networks & Volumes

### Implemented

#### Named Network

```yaml
networks:
  visitor-network:
```

#### Named Volumes

```yaml
volumes:
  postgres-data:
  redis-data:
```

#### Labels

Added labels for better service identification and organization.

### Result

✅ Containers communicate using custom network.

✅ Database and Redis data persist across container recreation.

---

## Task 6: Scaling (Bonus)

### Command Used

```bash
docker compose up --scale web=3
```

### What Happened?

Docker Compose failed because all Flask containers attempted to bind to the same host port:

```text
Bind for 0.0.0.0:5000 failed:
port is already allocated
```

### Why Does Scaling Fail?

When multiple containers expose:

```yaml
ports:
  - "5000:5000"
```

Only one container can use host port 5000.

Additional replicas cannot bind to the same port.

### Real-World Solution

Use:

* Load Balancer (Nginx)
* Reverse Proxy
* Docker Swarm
* Kubernetes Services

to distribute traffic across multiple replicas.

---

# RESULT

### Application Features

* Add Visitors
* Retrieve Visitor Records
* Store Data in PostgreSQL
* Track Homepage Visits using Redis
* Multi-Container Deployment using Docker Compose
* Persistent Storage using Docker Volumes
* Container Communication using Docker Networks

### Project Files

* Flask Application
* Dockerfile
* Docker Compose Configuration
* PostgreSQL Database
* Redis Cache

### Screenshots

#### Application Home Page



#### Add Visitor API



#### Get Visitors API



#### Docker Containers Running


---
# Learning Outcomes

By completing this project, I gained hands-on experience in building and managing multi-container applications using Docker Compose. I learned how to connect services using Docker Networks, persist data with Volumes, and manage service dependencies using Healthchecks and `depends_on`. The project also helped me understand PostgreSQL and Redis integration with Flask applications, along with implementing restart policies and custom Docker image builds for real-world deployments.



