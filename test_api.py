"""
Automated Test Suite for CRUD Task API
Verifies all 10 required test scenarios and HTTP status codes.
"""

from fastapi.testclient import TestClient
from main import app, tasks_db

client = TestClient(app)


def reset_database():
    """Reset in-memory data store to initial state before each test run."""
    tasks_db.clear()
    tasks_db.extend([
        {"id": 1, "title": "Learn FastAPI basics", "done": True},
        {"id": 2, "title": "Build a CRUD Task API", "done": False},
        {"id": 3, "title": "Test endpoints with Swagger UI", "done": False},
    ])


def test_get_root():
    """Test GET / returns API metadata and 200 status."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Task API"
    assert data["version"] == "1.0"
    assert "/tasks" in data["endpoints"]


def test_get_health():
    """Test GET /health returns status ok and 200 status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_tasks():
    """Test GET /tasks returns full list of tasks and 200 status."""
    reset_database()
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 3
    assert tasks[0]["id"] == 1


def test_get_task_by_id_success():
    """Test GET /tasks/1 returns single task and 200 status."""
    reset_database()
    response = client.get("/tasks/1")
    assert response.status_code == 200
    task = response.json()
    assert task["id"] == 1
    assert task["title"] == "Learn FastAPI basics"


def test_get_task_by_id_not_found():
    """Test GET /tasks/99 returns 404 Not Found."""
    reset_database()
    response = client.get("/tasks/99")
    assert response.status_code == 404
    assert "detail" in response.json()


def test_post_task_success():
    """Test POST /tasks creates task, assigns ID, defaults done=false, returns 201."""
    reset_database()
    payload = {"title": "Buy milk"}
    response = client.post("/tasks", json=payload)
    assert response.status_code == 201
    created_task = response.json()
    assert created_task["id"] == 4
    assert created_task["title"] == "Buy milk"
    assert created_task["done"] is False


def test_post_task_empty_title():
    """Test POST /tasks with empty or whitespace title returns 400 Bad Request."""
    reset_database()
    # Test empty string
    response = client.post("/tasks", json={"title": ""})
    assert response.status_code == 400
    
    # Test whitespace string
    response = client.post("/tasks", json={"title": "   "})
    assert response.status_code == 400


def test_put_task_success():
    """Test PUT /tasks/1 updates task title and done status, returns 200."""
    reset_database()
    payload = {"title": "Master FastAPI basics", "done": True}
    response = client.put("/tasks/1", json=payload)
    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["id"] == 1
    assert updated_task["title"] == "Master FastAPI basics"
    assert updated_task["done"] is True


def test_put_task_not_found():
    """Test PUT /tasks/99 returns 404 Not Found."""
    reset_database()
    payload = {"title": "Non-existent task"}
    response = client.put("/tasks/99", json=payload)
    assert response.status_code == 404


def test_put_task_invalid_title():
    """Test PUT /tasks/1 with empty title returns 400 Bad Request."""
    reset_database()
    payload = {"title": "   "}
    response = client.put("/tasks/1", json=payload)
    assert response.status_code == 400


def test_delete_task_success():
    """Test DELETE /tasks/1 removes task and returns 204 No Content."""
    reset_database()
    response = client.delete("/tasks/1")
    assert response.status_code == 204
    assert response.text == ""  # Empty body
    
    # Verify task is deleted
    get_response = client.get("/tasks/1")
    assert get_response.status_code == 404


def test_delete_task_not_found():
    """Test DELETE /tasks/99 returns 404 Not Found."""
    reset_database()
    response = client.delete("/tasks/99")
    assert response.status_code == 404
