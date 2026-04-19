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
| **Frontend** | HTML5 / CSS3 / Vanilla JS | - |
| **Language** | Python | 3.10+ |
| **Framework** | Flask | 3.1.3 |
| **Database** | MongoDB (via PyMongo) | 4.16.0 |
| **Cloud DB** | MongoDB Atlas | - |
| **TLS/Certs** | Certifi | 2026.2.25 |
| **Environment** | python-dotenv | 1.2.2 |
| **Testing** | pytest | 9.0.3 |
| **WSGI Toolkit** | Werkzeug | 3.1.8 |

---

## ✨ Key Features

- **Blueprint Architecture** - Routes, error handlers, and models are separated into Flask Blueprints for clean organization.
- **MongoDB Atlas Integration** - Cloud-native database connectivity with TLS/SSL certificate validation via `certifi`.
- **Centralized Error Handling** - A dedicated errors Blueprint returns consistent JSON for `404`, `400`, `405`, and `422` cases.
- **Full CRUD on Tasks** - Create, read, update, and delete tasks with proper HTTP semantics (`GET`, `POST`, `PUT`, `DELETE`).
- **Task Lists Support** - Create and manage named task lists, and filter tasks by `list_id`.
- **Interactive Frontend UI** - Includes a browser-based todo interface with inline edit/save controls, list management, and a polished animated background.
- **Input Validation** - Every write operation validates incoming JSON and returns clear error responses.
- **ObjectId-Safe Responses** - MongoDB `ObjectId` fields are converted to strings for valid JSON output.
- **Environment-Driven Config** - All secrets and connection strings live in `.env`, with no credentials committed.
- **Test Suite Included** - A `tests/` directory keeps route and behavior tests close to the app.

---

## 🎨 Frontend UI

### Dark Theme Design
The frontend features a modern dark theme optimized for extended use:

- **Cosmic Gradient Background** - Dynamic gradient with radial accent layers (blue, purple, green) that evolve across the viewport
- **Animated Starfield** - Subtle drifting star particles for visual depth and motion
- **Glowing Orbs** - Smooth floating animation with blur effects creating an immersive backdrop
- **Semi-Transparent Cards** - Task items and containers use frosted glass aesthetics with `rgba()` layers

### Interactive Features
- **Inline Edit Mode** - Click the pencil icon on any task to edit the title inline; press `Enter` to save or `Escape` to cancel
- **Toggle Completion** - Click the checkbox to mark tasks complete/incomplete
- **Instant Delete** - Click the delete (✕) icon to remove a task immediately
- **List Management** - Create new lists, switch between them, and add tasks inside a selected list.
- **Real-Time Sync** - All changes update the backend instantly via REST API calls

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

Create a `.env` file in the project root and add your MongoDB connection string:

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
3. Double-check the connection string - the env variable name is `MONDGO_DB_CON_STRING` (note the typo - matches the source code intentionally).
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

The API exposes task and list endpoints. The frontend UI calls these directly to keep tasks and lists in sync.

### Endpoints Overview

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/tasks` | Retrieve all tasks or tasks filtered by `list_id` |
| `POST` | `/tasks` | Create a new task |
| `GET` | `/tasks/<id>` | Retrieve a single task by ID |
| `PUT` | `/tasks/<id>` | Update a task by ID |
| `DELETE` | `/tasks/<id>` | Delete a task by ID |
| `GET` | `/lists` | Retrieve all lists |
| `POST` | `/lists` | Create a new list |
| `GET` | `/lists/<list_id>` | Retrieve a single list by ID |
| `PUT` | `/lists/<list_id>` | Rename a list |
| `DELETE` | `/lists/<list_id>` | Delete a list and all its tasks |

---

### `GET /tasks` - List all tasks

```bash
curl http://127.0.0.1:5000/tasks
```

**Optional filter by list:**

```bash
curl http://127.0.0.1:5000/tasks?list_id=<list_id>
```

**Response `200 OK`:**

```json
[
  {
    "_id": "664f1c2a8e442d001f3j9c11",
    "title": "Learn Flask",
    "completed": false,
    "list_id": "7f3a2b1c-4d5e-6f7g-8h9i-0j1k2l3m4n5o"
  }
]
```

---

### `POST /tasks` - Create a task

```bash
curl -X POST http://127.0.0.1:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Write unit tests", "list_id": "<list_id>"}'
```

**Response `201 Created`:**

```json
{
  "success": true,
  "new_task": {
    "_id": "664f1d359e4b2d001f3a9c99",
    "title": "Write unit tests",
    "completed": false,
    "list_id": "<list_id>"
  }
}
```

---

### `PUT /tasks/<id>` - Update a task

```bash
curl -X PUT http://127.0.0.1:5000/tasks/664f1d3b9e4b2d001f3a9c99 \
  -H "Content-Type: application/json" \
  -d '{"title": "Write unit tests", "completed": true}'
```

**Response `200 OK`:**

```json
"Task 664f1d3b9e4b2d001f3a9c99 updated successfully"
```

---

### `DELETE /tasks/<id>` - Delete a task

```bash
curl -X DELETE http://127.0.0.1:5000/tasks/66381d3h9e4b2d041f3a9c99
```

**Response `200 OK`:**

```json
"Task with ID 664f1d3b9e4b2d001f3a9c99 has been successfully deleted"
```

---

### `GET /lists` - Retrieve all lists

```bash
curl http://127.0.0.1:5000/lists
```

**Response `200 OK`:**

```json
[
  {
    "_id": "64d0a2f5f4c3b1a0012d3e4f",
    "id": "7f3a2b1c-4d5e-6f7g-8h9i-0j1k2l3m4n5o",
    "name": "Work"
  }
]
```

---

### `POST /lists` - Create a list

```bash
curl -X POST http://127.0.0.1:5000/lists \
  -H "Content-Type: application/json" \
  -d '{"name": "Work"}'
```

**Response `201 Created`:**

```json
{
  "success": true,
  "data": {
    "_id": "64d0a2f5f4c3b1a0012d3e4f",
    "id": "7f3a2b1c-4d5e-6f7g-8h9i-0j1k2l3m4n5o",
    "name": "Work"
  }
}
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
MyFirstFlask1/
│
├── app.py                    # Flask application entry point and blueprint registration
├── requirements.txt          # Python dependency list
├── README.md                 # Project documentation
├── .env                      # Local environment configuration (not committed)
│
├── config/                   # Database and error handler setup
│   ├── database.py           # MongoDB client initialization and collection helper
│   └── errors.py             # Centralized Flask error handlers
│
├── routes/                   # HTTP route handlers organized by feature
│   ├── tasks.py              # Task CRUD routes and list filtering support
│   └── lists.py              # List CRUD routes
│
├── models/                   # Business logic and data access
│   ├── task.py               # Task validation, persistence, and updates
│   └── list.py               # List creation, update, delete, and serialization
│
├── templates/                # HTML frontend
│   └── index.html            # Interactive todo UI with task/list toolbar
│
├── static/                   # CSS and frontend assets
│   └── style.css             # Dark theme, animated background, responsive layout
│
└── tests/                    # pytest tests for route and model behavior
```

### Request Flow

```
Browser (index.html)
     │
     ├─── GET / ──────────────▶ Render UI and load current lists/tasks
     │
     ├─── JS fetch /lists    ▶ List management
     ├─── JS fetch /tasks    ▶ Task CRUD and list filtering
     ▼
 app.py  ──── registers ────▶ tasks_bp, lists_bp, errors_bp
     │
     ├─── routes/tasks.py    ▶ Task endpoints and query handling
     ├─── routes/lists.py    ▶ List endpoints
     │
     ▼
 models/task.py            ▶ Validate task data and interact with MongoDB
 models/list.py            ▶ Persist lists, serialize IDs, delete associated tasks
     │
     ▼
 config/database.py        ▶ MongoDB client / collection helpers
 config/errors.py          ▶ Error translation to JSON responses
```

---


<details>
<summary>📐 <strong>Code Style Guidelines</strong></summary>

<br/>

- Use descriptive variable names - clarity beats brevity.
- Keep route handlers thin: dispatch to model functions, don't write logic in routes.
- All error cases should raise Werkzeug HTTP exceptions (e.g., `NotFound`, `BadRequest`) - never return raw error strings from routes.
- Use type hints where practical.
- Add a docstring to any new function that isn't immediately self-explanatory.

</details>

---

<div align="center">

Made with ☕ and hours in Fittusi's DevOps class.

⭐ **If this project helped you, consider giving it a star!** ⭐

</div>
