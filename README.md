# microservices-event-driven-simple-vote-app

This guide assumes users have basic familiarity with Python, Java, Node.js, React, Docker (optional), and Git.

📘 ReadMe.txt — Microservices Voting System
Author: Moses
Version: 1.0
Repository: https://github.com/herbert-moses/<your-repo-name>](https://github.com/herbertmoses/microservices-event-driven-simple-vote-app

─────────────────────────────────────────────
🧭 Project Overview
─────────────────────────────────────────────
This is a complete event-driven, microservices-based voting application with the following tech stack:

🧑 User Login Service: Django + PostgreSQL
🧠 Master Session Manager: Flask + Redis
🗳️ Voting Service: Spring Boot + MongoDB
⚙️ Worker Service: FastAPI (for vote aggregation)
📊 Results Viewer: Node.js + React
─────────────────────────────────────────────
📂 Folder Structure
─────────────────────────────────────────────
project-root/
├── login_project/ # Django + PostgreSQL
├── master-app/ # Flask + Redis
├── voting-app/ # SpringBoot + MongoDB
├── worker-app/ # FastAPI vote summarizer
└── results-app/ # Node.js backend + React frontend

─────────────────────────────────────────────
⚙️ Prerequisites
─────────────────────────────────────────────
Install the following software before proceeding:

Python 3.13.x
PostgreSQL 14+
Redis 7.x
MongoDB 6.x+
Java 21 (JDK 21)
Node.js v18+
npm v9+
Maven 3.8+
Git
─────────────────────────────────────────────
🚀 Service Setup Instructions
─────────────────────────────────────────────

─────────────────────────────────────────────
1️⃣ login_project (Django + PostgreSQL)
─────────────────────────────────────────────
cd login_project
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

🔧 Edit settings.py:

Set PostgreSQL credentials (user: xxx, password: xyz)
DB name: zzz
💾 Run migrations:
python manage.py migrate

▶️ Start server:
python manage.py runserver
→ Accessible at http://localhost:8000

─────────────────────────────────────────────
2️⃣ master-app (Flask + Redis)
─────────────────────────────────────────────
cd master-app
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

▶️ Start Redis server (in a separate terminal):
redis-server

▶️ Start Flask app:
python app.py
→ Runs at http://localhost:5001

─────────────────────────────────────────────
3️⃣ voting-app (SpringBoot + MongoDB)
─────────────────────────────────────────────
cd voting-app

🔧 Check src/main/resources/application.properties:
spring.data.mongodb.uri=mongodb://localhost:27017/votingdb

▶️ Start Spring Boot App (from IDE or terminal):
mvn spring-boot:run
→ Runs at http://localhost:8082/vote?username=someuser

─────────────────────────────────────────────
4️⃣ worker-app (FastAPI + MongoDB Reader)
─────────────────────────────────────────────
cd worker-app
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

▶️ Start FastAPI app:
uvicorn app:app --reload --port 8003
→ Endpoint: http://localhost:8003/summary

─────────────────────────────────────────────
5️⃣ results-app (Node.js + React)
─────────────────────────────────────────────
cd results-app/server
npm install
node index.js
→ Backend server runs at http://localhost:8084

cd ../client
npm install
npm run build
-> React listens to node backend server and runs the frontend UI

(Optional) Configure CORS or proxy if accessing API via frontend.

─────────────────────────────────────────────
🔁 Application Flow Summary
─────────────────────────────────────────────

User logs in via Django (http://localhost:8000)
Django notifies Flask (session manager)
Redirects to Spring Boot voting app with ?username
Vote stored in MongoDB
FastAPI aggregates votes
React frontend fetches results from FastAPI
User sees live voting results
─────────────────────────────────────────────
✅ Final Notes
─────────────────────────────────────────────

All services should run simultaneously for full functionality.
Votes are session-managed via Redis.
Use Postman or browser to test endpoints independently.
To reset state, clear MongoDB (db.votes.deleteMany({})) and Redis (flushall).
─────────────────────────────────────────────
📮 License & Acknowledgment
─────────────────────────────────────────────
MIT License — free to use, distribute, and modify.

