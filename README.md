<div align="center">

<!-- PROJECT BANNER -->
<img src="https://placehold.co/900x200/1a1a2e/ffffff?text=Flask+API+MiniProject&font=montserrat" alt="Flask API MiniProject Banner" width="100%" />

<br/>

# ⚡ Flask API MiniProject

### A clean, modular REST API built with Flask and MongoDB - engineered for clarity, extensibility, and real world patterns.

<br/>

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/atlas)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

</div>

---

## 📖 Table of Contents

- [Tech Stack](#-tech-stack)
- [Key Features](#-key-features)
- [Frontend UI](#-frontend-ui)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [Contributing](#-contributing)

---

## 🛠 Tech Stack

| Layer | Technology | Version |
|---|---|---|
| **Frontend** | HTML5 / CSS3 / Vanilla JS | — |
| **Language** | Python | 3.10+ |
| **Framework** | Flask | 3.1.3 |
| **Database** | MongoDB (via PyMongo) | 4.16.0 |
| **Cloud DB** | MongoDB Atlas | — |
| **TLS/Certs** | Certifi | 2026.2.25 |
| **Environment** | python-dotenv | 1.2.2 |
| **Testing** | pytest | 9.0.3 |
| **WSGI Toolkit** | Werkzeug | 3.1.8 |

---

## ✨ Key Features

- **Blueprint Architecture** — Routes, error handlers, and models are fully separated into Flask Blueprints, making the codebase easy to navigate and scale.
- **MongoDB Atlas Integration** — Cloud-native database connectivity with TLS/SSL certificate validation via `certifi`, production-ready out of the box.
- **Centralized Error Handling** — A dedicated errors Blueprint catches `404 NotFound`, `400 BadRequest`, `405 MethodNotAllowed`, and `422 UnprocessableEntity` with clean, consistent JSON responses.
- **Full CRUD on Tasks** — Create, read, update, and delete tasks with proper HTTP semantics (`GET`, `POST`, `PUT`, `DELETE`).
- **Interactive Frontend UI** — Includes a browser-based todo interface with inline edit/save controls, responsive cards, and an animated dark background.
- **Input Validation** — Every write operation validates and sanitizes incoming data before it touches the database.
- **ObjectId-Safe Responses** — MongoDB's `ObjectId` is automatically serialized to strings, so responses are always valid JSON.
- **Environment-Driven Config** — All secrets and connection strings live in `.env` — no credentials ever touch the codebase.
- **Test Suite Included** — A `tests/` directory keeps quality gates close to the code.

---

## 🎨 Frontend UI

### Dark Theme Design
The frontend features a modern dark theme optimized for extended use:

- **Cosmic Gradient Background** — Dynamic gradient with radial accent layers (blue, purple, green) that evolve across the viewport
- **Animated Starfield** — Subtle drifting star particles for visual depth and motion
- **Glowing Orbs** — Smooth floating animation with blur effects creating an immersive backdrop
- **Semi-Transparent Cards** — Task items and containers use frosted glass aesthetics with `rgba()` layers

### Interactive Features
- **Inline Edit Mode** — Click the pencil icon on any task to edit the title inline; press `Enter` to save or `Escape` to cancel
- **Toggle Completion** — Click the checkbox to mark tasks complete/incomplete
- **Instant Delete** — Click the delete (✕) icon to remove a task immediately
- **Real-Time Sync** — All changes update the backend instantly via REST API calls

### Responsive Layout
- Centered container layout that works on desktop and tablet sizes
- Smooth hover transitions on task cards and buttons
- Touch-friendly button sizing and spacing
- Error messages auto-dismiss after 4 seconds

---

### Prerequisites

Make sure you have the following installed before proceeding:

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- A [MongoDB Atlas](https://www.mongodb.com/atlas) account (free tier works great)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/GuyGuyPeres/Flask_API_MiniProject.git
cd Flask_API_MiniProject
```

**2. Create and activate a virtual environment**

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file in the project root:

```bash
cp .env.example .env   # if provided, otherwise create manually
```

Then open `.env` and fill in your values:

```env
MONDGO_DB_CON_STRING=mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
```

> ⚠️ **Never commit your `.env` file.** It is already listed in `.gitignore`.

<details>
<summary>📋 <strong>Troubleshooting: MongoDB Connection Issues</strong></summary>

<br/>

**Problem:** `ServerSelectionTimeoutError` when starting the app.

**Checklist:**
1. Confirm your Atlas cluster is not paused (free tier auto-pauses after inactivity).
2. Whitelist your IP in Atlas under **Network Access → Add IP Address**.
3. Double-check the connection string — the env variable name is `MONDGO_DB_CON_STRING` (note the typo — matches the source code intentionally).
4. Make sure `certifi` is installed: `pip show certifi`.

**Problem:** `ModuleNotFoundError` on startup.

Make sure your virtual environment is activated before running the app.

</details>

### Run the App

```bash
python app.py
```

The server starts in debug mode at:

```
http://127.0.0.1:5000
```

Then open the web UI at:

```
http://127.0.0.1:5000/
```

### Run Tests

```bash
pytest tests/ -v
```

---

## 💡 Usage

All endpoints are prefixed at `/tasks`. The API consumes and produces `application/json`.

### Endpoints Overview

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/tasks` | Retrieve all tasks |
| `POST` | `/tasks` | Create a new task |
| `GET` | `/tasks/<id>` | Retrieve a single task by ID |
| `PUT` | `/tasks/<id>` | Update a task by ID |
| `DELETE` | `/tasks/<id>` | Delete a task by ID |

---

### `GET /tasks` — List all tasks

```bash
curl http://127.0.0.1:5000/tasks
```

**Response `200 OK`:**

```json
[
  {
    "_id": "664f1c2a8e442d001f3j9c11",
    "title": "Learn Flask",
    "completed": false
  },
  {
    "_id": "664f1c2a6e4b2d001g3a9c12",
    "title": "Build API",
    "completed": true
  }
]
```

---

### `POST /tasks` — Create a task

```bash
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Write unit tests"}'
```

**Response `200 OK`:**

```json
{
  "success": true,
  "new_task": {
    "_id": "664f1d359e4b2d001f3a9c99",
    "title": "Write unit tests",
    "completed": false
  }
}
```

---

### `PUT /tasks/<id>` — Update a task

```bash
curl -X PUT http://127.0.0.1:5000/tasks/664f1d3bld4b2d001f3a9c99 \
  -H "Content-Type: application/json" \
  -d '{"title": "Write unit tests", "completed": true}'
```

**Response `200 OK`:**

```json
"Task 664f1d3b9e4b2d09pf3a9c99 updated successfully"
```

---

### `DELETE /tasks/<id>` — Delete a task

```bash
curl -X DELETE http://127.0.0.1:5000/tasks/66381d3h9e4b2d041f3a9c99
```

**Response `200 OK`:**

```json
"Task with ID 664f1d3b9esg2d001f3a9c99 has been successfully deleted"
```

---

### Error Responses

All errors return a consistent JSON structure:

```json
{
  "status": 404,
  "error": "NotFound",
  "message": "Task with ID xyz not found"
}
```

---

## 🏗 Architecture

### Folder Structure

```
Flask_API_MiniProject/
│
├── 📄 app.py                   # Application entry point — creates the Flask app & registers Blueprints
├── 📄 database.py              # MongoDB client setup and collection reference
│
├── 📄 HAFRADA_routes.py        # Blueprint: URL routes and HTTP method dispatching
├── 📄 HAFRADA_models.py        # Blueprint: Business logic and database operations
├── 📄 HAFRADA_errors.py        # Blueprint: Centralized error handlers
│
├── 📁 templates/               # HTML frontend
│   └── index.html              #   ↳ Interactive todo UI with dark theme
│
├── 📁 static/                  # CSS and client-side assets
│   └── style.css               #   ↳ Dark theme, animations, responsive layout
│
├── 📁 archive/                 # Historical versions and experimental code
│
├── 📁 tests/                   # pytest test suite
│   ├── test_routes.py          #   ↳ Route-level integration tests
│   └── test_models.py          #   ↳ Model/logic unit tests
│
├── 📄 requirements.txt         # Pinned Python dependencies
├── 📄 .gitignore               # Git exclusions (venv, .env, __pycache__, etc.)
└── 📄 README.md                # You are here
```

### Request Flow

```
Browser (index.html)
     │
     ├─── GET / ──────────────┐
     │                        │
     │   ┌──────────────────────────────┐
     │   │  Render UI (dark theme)     │
     │   │  - Starfield background     │
     │   │  - Task list                │
     │   │  - Edit/Delete controls     │
     │   └──────────────────────────────┘
     │
     ├─── JavaScript API Calls ────────┐
     │   (fetch to /tasks)             │
     │                                 │
     ▼                                 ▼
HTTP Request
     │
     ▼
 app.py  ──── registers ────▶  errors_bp (HAFRADA_errors.py)
     │                              ↑ catches unhandled exceptions
     │
     ▼
HAFRADA_routes.py  (tasks_bp)
     │  dispatches by HTTP method
     ▼
HAFRADA_models.py
     │  validates input, calls DB
     ▼
database.py  ──▶  MongoDB Atlas
     │
     ▼
JSON Response ──────────────┐
                            │
                            ▼
                  Update DOM & UI
                  (smooth transitions)
```

---


<details>
<summary>📐 <strong>Code Style Guidelines</strong></summary>

<br/>

- Use descriptive variable names — clarity beats brevity.
- Keep route handlers thin: dispatch to model functions, don't write logic in routes.
- All error cases should raise Werkzeug HTTP exceptions (e.g., `NotFound`, `BadRequest`) — never return raw error strings from routes.
- Use type hints where practical.
- Add a docstring to any new function that isn't immediately self-explanatory.

</details>

---

<div align="center">

Made with ☕ and hours in Fittusi's DevOps class.

⭐ **If this project helped you, consider giving it a star!** ⭐

</div>
