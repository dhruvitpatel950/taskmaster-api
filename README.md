# 🚀 TaskMaster API

> A robust, production-ready Task Management API built with Django REST Framework, Docker, and Celery.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-Async-37814A?style=for-the-badge&logo=celery&logoColor=white)

## 🌟 Features

* **🏢 Multi-Tenancy:** Users can only access their own tasks and projects.
* **🔐 Secure Auth:** Token-based authentication system.
* **⚡ Asynchronous Tasks:** Heavy operations (emails/reports) offloaded to **Celery + Redis**.
* **🐳 Dockerized:** Fully containerized setup (Django, Postgres, Redis, Worker) via Docker Compose.
* **📡 Event-Driven:** Django Signals used for decoupled side-effects (e.g., auto-updating project timestamps).
* **🔎 Power Search:** Filtering, Searching, and Pagination built-in.
* **📚 Self-Documenting:** Interactive Swagger/OpenAPI documentation (`/api/docs/`).

## 🛠️ Tech Stack

* **Backend:** Django 5, Django REST Framework
* **Database:** PostgreSQL (Docker)
* **Async Queue:** Celery, Redis
* **Infrastructure:** Docker, Docker Compose
* **Documentation:** drf-spectacular (OpenAPI 3.0)

## 🚀 Quick Start (Docker)

The easiest way to run the project. No local Python/Postgres required.

# 1. Clone the repo
git clone [https://github.com/YOUR_USERNAME/taskmaster.git](https://github.com/YOUR_USERNAME/taskmaster.git)
cd taskmaster

# 2. Build and Run
docker compose up --build

The API will be available at `http://127.0.0.1:8000/api/`.

### 🔑 First Time Setup

Since the database is fresh, create a superuser inside the container:

docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser

## 📖 API Documentation

Once running, visit the interactive API docs:

* **Swagger UI:** `http://127.0.0.1:8000/api/docs/`
* **ReDoc:** `http://127.0.0.1:8000/api/redoc/`

## 🧪 Testing Async Tasks

To test the background worker:

1. Send a **POST** request to `/api/tasks/`.
2. Watch the Docker logs for the `worker` container.
3. You will see: `📧 Email sent to admin!` (simulated delay).

## 📂 Project Structure

taskmaster/
├── config/           # Project settings & URL routing
├── tasks/            # Main application logic
│   ├── models.py     # Database schema
│   ├── views.py      # API Controllers
│   ├── serializers.py# JSON Conversion
│   ├── signals.py    # Event triggers
│   └── tasks.py      # Celery background jobs
├── docker-compose.yml# Container orchestration
└── Dockerfile        # Image definition

*Built with ❤️ by [Dhruvit Patel]*

