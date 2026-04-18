<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask_API_MiniProject Documentation</title>
    <style>
        :root {
            --primary-color: #2c3e50;
            --accent-color: #3498db;
            --bg-color: #f8f9fa;
            --text-color: #333;
            --code-bg: #e9ecef;
            --border-color: #dee2e6;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 900px;
            margin: 40px auto;
            background: #fff;
            padding: 40px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border-radius: 8px;
        }

        header {
            text-align: center;
            border-bottom: 2px solid var(--accent-color);
            padding-bottom: 20px;
            margin-bottom: 30px;
        }

        .banner {
            width: 100%;
            height: 200px;
            background-color: #eee;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 20px;
            border-radius: 4px;
            color: #777;
            font-weight: bold;
        }

        .badges {
            margin: 20px 0;
        }

        .badges img {
            margin: 0 5px;
        }

        h1, h2, h3 {
            color: var(--primary-color);
        }

        h2 {
            border-left: 5px solid var(--accent-color);
            padding-left: 15px;
            margin-top: 40px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }

        table th, table td {
            padding: 12px;
            border: 1px solid var(--border-color);
            text-align: left;
        }

        table th {
            background-color: var(--accent-color);
            color: white;
        }

        code {
            background-color: var(--code-bg);
            padding: 2px 5px;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
        }

        pre {
            background-color: var(--primary-color);
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            font-family: 'Courier New', Courier, monospace;
        }

        .features ul {
            list-style-type: none;
            padding: 0;
        }

        .features li {
            margin-bottom: 10px;
            padding-left: 25px;
            position: relative;
        }

        .features li::before {
            content: "🚀";
            position: absolute;
            left: 0;
        }

        details {
            background: #f1f1f1;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
            margin: 10px 0;
        }

        summary {
            font-weight: bold;
        }

        footer {
            text-align: center;
            margin-top: 50px;
            font-size: 0.9em;
            color: #777;
        }
    </style>
</head>
<body>

<div class="container">
    <header>
        <div class="banner">PROJECT BANNER PLACEHOLDER</div>
        <h1>Flask_API_MiniProject</h1>
        <p>A robust, modular Todo API built with Flask and MongoDB, featuring custom error handling and clean architecture.</p>
        
        <div class="badges">
            <img src="https://img.shields.io/badge/python-3.12+-blue.svg" alt="Python">
            <img src="https://img.shields.io/badge/flask-3.1.3-green.svg" alt="Flask">
            <img src="https://img.shields.io/badge/database-MongoDB-brightgreen.svg" alt="MongoDB">
            <img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="License">
        </div>
    </header>

    <section id="tech-stack">
        <h2>🚀 Tech Stack</h2>
        <table>
            <thead>
                <tr>
                    <th>Category</th>
                    <th>Technology</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Backend</td>
                    <td>Python 3.12+, Flask 3.1.3</td>
                </tr>
                <tr>
                    <td>Database</td>
                    <td>MongoDB Atlas (PyMongo)</td>
                </tr>
                <tr>
                    <td>Environment</td>
                    <td>python-dotenv</td>
                </tr>
                <tr>
                    <td>Testing</td>
                    <td>Pytest</td>
                </tr>
                <tr>
                    <td>Security</td>
                    <td>Certifi (SSL/TLS support)</td>
                </tr>
            </tbody>
        </table>
    </section>

    <section id="features" class="features">
        <h2>✨ Key Features</h2>
        <ul>
            <li><strong>Modular Architecture:</strong> Separation of concerns using Blueprints for routes and error handling.</li>
            <li><strong>Full CRUD Operations:</strong> Seamlessly Create, Read, Update, and Delete tasks in a MongoDB collection.</li>
            <li><strong>Custom Error Management:</strong> Centralized error handling for 404, 400, 405, and 403 status codes.</li>
            <li><strong>Dynamic ID Handling:</strong> Automatic conversion between MongoDB ObjectIDs and JSON-friendly strings.</li>
            <li><strong>Environment Safety:</strong> Sensitive database credentials managed via .env files.</li>
        </ul>
    </section>

    <section id="architecture">
        <h2>📂 Project Architecture</h2>
        <pre>
Flask_API_MiniProject/
├── archive/                # Legacy code and previous iterations
├── tests/                  # Pytest suite for API endpoints
├── app.py                  # Application entry point & Blueprint registration
├── database.py             # MongoDB connection logic
├── HAFRADA_routes.py       # API endpoint definitions (Blueprints)
├── HAFRADA_models.py       # Business logic and database interactions
├── HAFRADA_errors.py       # Custom global error handlers
├── requirements.txt        # Project dependencies
└── .env                    # Environment variables (Internal only)
        </pre>
    </section>

    <section id="getting-started">
        <h2>🛠️ Getting Started</h2>
        <h3>Installation</h3>
        <ol>
            <li><strong>Clone the repository:</strong>
                <pre>git clone https://github.com/yourusername/Flask_API_MiniProject.git</pre>
            </li>
            <li><strong>Install dependencies:</strong>
                <pre>pip install -r requirements.txt</pre>
            </li>
            <li><strong>Setup .env:</strong> Create a file named <code>.env</code> with your <code>MONDGO_DB_CON_STRING</code>.</li>
            <li><strong>Run:</strong>
                <pre>python app.py</pre>
            </li>
        </ol>
    </section>

    <section id="usage">
        <h2>📖 Usage Examples</h2>
        <h3>Get All Tasks</h3>
        <code>GET /tasks</code>
        <pre>curl http://127.0.0.1:5000/tasks</pre>

        <details>
            <summary>View API Endpoint Table</summary>
            <table>
                <tr>
                    <th>Method</th>
                    <th>Endpoint</th>
                    <th>Description</th>
                </tr>
                <tr>
                    <td>GET</td>
                    <td>/tasks</td>
                    <td>Retrieve all tasks.</td>
                </tr>
                <tr>
                    <td>POST</td>
                    <td>/tasks</td>
                    <td>Create a new task.</td>
                </tr>
                <tr>
                    <td>PUT</td>
                    <td>/tasks/&lt;id&gt;</td>
                    <td>Update a task.</td>
                </tr>
                <tr>
                    <td>DELETE</td>
                    <td>/tasks/&lt;id&gt;</td>
                    <td>Delete a task.</td>
                </tr>
            </table>
        </details>
    </section>

    <section id="license">
        <h2>⚖️ License</h2>
        <p>Distributed under the MIT License.</p>
    </section>

    <footer>
        <p>Maintained by Guy Peres | 2026 Flask_API_MiniProject</p>
    </footer>
</div>

</body>
</html>