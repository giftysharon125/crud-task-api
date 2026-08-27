# CRUD Task API

A beginner-friendly REST-style Task Management API built with **Python 3.10+** and **FastAPI**. This API allows users to perform full CRUD (Create, Read, Update, Delete) operations on a task list stored in-memory.

---

## 📖 Description

The **CRUD Task API** provides a backend Web API that enables client applications (such as web frontends, mobile apps, or API testing clients like Swagger UI) to interact with a list of tasks. Each task consists of a unique numeric `id`, a string `title`, and a boolean `done` status flag indicating completion. Data is kept in-memory for simple, lightweight execution.

---

## 🛠️ Technologies Used

* **Python 3.10+**: Core programming language.
* **FastAPI**: Modern, high-performance web framework for building APIs with Python.
* **Pydantic**: Data validation and settings management using Python type hints.
* **Uvicorn**: Lightning-fast ASGI server implementation for Python.
* **Swagger UI**: Interactive automatic documentation automatically hosted by FastAPI at `/docs`.

---

## ⚙️ Installation

Follow these steps to set up the project locally:

1. **Clone or navigate to the project directory:**
   ```bash
   cd CRUD_TASK_API
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   * **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   * **Windows (CMD):**
     ```cmd
     .\venv\Scripts\activate.bat
     ```
   * **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the API

Start the FastAPI development server with automatic reloading enabled using either command:

```bash
uvicorn main:app --reload
```
*or using FastAPI CLI:*
```bash
fastapi dev main.py
```

Once started, the server will run locally at `http://127.0.0.1:8000` (or `http://localhost:8000`).

---

## 📌 API Endpoints Summary

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | API Root Information & Metadata |
| `GET` | `/health` | Health Check Endpoint |
| `GET` | `/tasks` | Retrieve all tasks |
| `GET` | `/tasks/{id}` | Retrieve a single task by ID |
| `POST` | `/tasks` | Create a new task |
| `PUT` | `/tasks/{id}` | Update an existing task's title/done status |
| `DELETE` | `/tasks/{id}` | Delete a task by ID |

---

## 📄 Swagger UI Documentation

FastAPI automatically generates interactive API documentation powered by Swagger UI.

* **Swagger UI URL:** `http://localhost:8000/docs`

You can use Swagger's **Try it out** feature directly in your browser to execute requests against all endpoints without needing external tools.

### 📸 Screenshot Placeholder for Submission
```text
+-----------------------------------------------------------------------+
|                                                                       |
|                     [ ADD YOUR SWAGGER SCREENSHOT HERE ]              |
|                                                                       |
|   1. Open http://localhost:8000/docs in your browser.                 |
|   2. Expand any endpoint (e.g., POST /tasks) and click "Try it out".   |
|   3. Take a screenshot showing the endpoints and paste/embed it here! |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## 🧪 Testing Checklist & `curl` Examples

You can test every endpoint using `curl` commands in your terminal or via the `pytest` test suite included in `test_api.py`.

### 1. Root Information
* **Command:**
  ```bash
  curl -X GET "http://localhost:8000/"
  ```
* **Expected Status Code:** `200 OK`

### 2. Health Check
* **Command:**
  ```bash
  curl -X GET "http://localhost:8000/health"
  ```
* **Expected Status Code:** `200 OK`

### 3. Get All Tasks
* **Command:**
  ```bash
  curl -X GET "http://localhost:8000/tasks"
  ```
* **Expected Status Code:** `200 OK`

### 4. Get Task by ID (Existing Task)
* **Command:**
  ```bash
  curl -X GET "http://localhost:8000/tasks/1"
  ```
* **Expected Status Code:** `200 OK`

### 5. Get Task by ID (Non-existent Task)
* **Command:**
  ```bash
  curl -X GET "http://localhost:8000/tasks/99"
  ```
* **Expected Status Code:** `404 Not Found`

### 6. Create a New Task (Valid Input)
* **Command:**
  ```bash
  curl -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d "{\"title\": \"Buy milk\"}"
  ```
* **Expected Status Code:** `201 Created`

### 7. Create Task (Invalid/Empty Title)
* **Command:**
  ```bash
  curl -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d "{\"title\": \"\"}"
  ```
* **Expected Status Code:** `400 Bad Request`

### 8. Update Existing Task
* **Command:**
  ```bash
  curl -X PUT "http://localhost:8000/tasks/1" -H "Content-Type: application/json" -d "{\"title\": \"Master FastAPI\", \"done\": true}"
  ```
* **Expected Status Code:** `200 OK`

### 9. Delete Existing Task
* **Command:**
  ```bash
  curl -X DELETE "http://localhost:8000/tasks/1"
  ```
* **Expected Status Code:** `204 No Content` (Empty body)

### 10. Delete Non-existent Task
* **Command:**
  ```bash
  curl -X DELETE "http://localhost:8000/tasks/99"
  ```
* **Expected Status Code:** `404 Not Found`

---

## 🐙 GitHub Preparation & Step-by-Step Git Commands

To publish this project to GitHub:

1. **Initialize Git repository:**
   ```bash
   git init
   ```

2. **Add project files:**
   ```bash
   git add .
   ```

3. **Check status to confirm `.gitignore` is working:**
   ```bash
   git status
   ```

4. **Connect to your GitHub repository:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/crud-task-api.git
   git branch -M main
   ```

5. **Push commits to GitHub:**
   ```bash
   git push -u origin main
   ```

---

## 🏷️ Stage Commits Guide

Follow these commands to create incremental stage commits required by the assignment specification:

### **Stage 0: hello server**
```bash
git add main.py
git commit -m "Stage 0: hello server"
```

### **Stage 1: root and health endpoints**
```bash
git add main.py
git commit -m "Stage 1: root and health endpoints"
```

### **Stage 2: read endpoints with 404**
```bash
git add main.py
git commit -m "Stage 2: read endpoints with 404"
```

### **Stage 3: create with validation**
```bash
git add main.py
git commit -m "Stage 3: create with validation"
```

### **Stage 4: full CRUD**
```bash
git add main.py
git commit -m "Stage 4: full CRUD"
```

### **Stage 5: Swagger UI**
```bash
git add main.py
git commit -m "Stage 5: Swagger UI"
```

### **Stage 6: publish and docs**
```bash
git add .
git commit -m "Stage 6: publish and docs"
```

---

## 💡 Beginner Core Concepts Breakdown

Here is a simple explanation of fundamental backend API concepts used in this project:

* **What is an API?**
  API stands for *Application Programming Interface*. It acts as a bridge that allows different software applications (like a browser or mobile app and a server) to talk to each other and share data over the web.

* **What does CRUD mean?**
  CRUD represents the four fundamental operations of persistent data storage:
  * **C**reate: Add new data (Task).
  * **R**ead: Retrieve data.
  * **U**pdate: Modify existing data.
  * **D**elete: Remove data.

* **What is an Endpoint?**
  An endpoint is a specific URL path on the server (e.g., `/tasks` or `/health`) where the API listens for client requests to perform specific actions.

* **What do HTTP Methods mean?**
  * **GET**: Used to request and read data from the server without modifying anything.
  * **POST**: Used to send new data to the server to create a resource.
  * **PUT**: Used to update an existing resource on the server.
  * **DELETE**: Used to remove a resource from the server.

* **What is a Request vs. Response?**
  * **Request**: The message sent by the client to the server containing the HTTP method, endpoint path, headers, and optional body payload.
  * **Response**: The answer sent back by the server containing a status code, headers, and body payload (usually JSON).

* **What is JSON?**
  JSON (*JavaScript Object Notation*) is a lightweight, human-readable text format for storing and exchanging data structured in key-value pairs (e.g., `{"id": 1, "title": "Buy milk", "done": false}`).

* **What are HTTP Status Codes?**
  Status codes are 3-digit standard numbers returned by the server to inform the client about the outcome of their request:
  * `200 OK`: Successful read or update.
  * `201 Created`: Resource successfully created.
  * `204 No Content`: Resource successfully deleted; no response body returned.
  * `400 Bad Request`: The client's request was invalid (e.g., empty task title).
  * `404 Not Found`: The requested endpoint or resource ID does not exist.

* **What is Swagger UI?**
  Swagger UI is an interactive documentation page generated automatically by FastAPI at `/docs`. It lists all available endpoints, required request bodies, and lets developers test endpoints interactively in the browser.

* **Why does data disappear when the server restarts?**
  Because this API uses **in-memory storage** (`tasks_db` python list). The data lives only inside the running computer's RAM memory. When the server process stops, RAM is cleared. Persistent databases (like SQLite or PostgreSQL) store data on a hard disk to keep it after restarts.
