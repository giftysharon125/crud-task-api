"""
CRUD Task API - FastAPI Implementation
Week 2 Assignment

This module implements a beginner-friendly RESTful Task API using FastAPI.
Data is stored strictly in-memory.
"""

from typing import Optional, List
from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel, Field


# ==============================================================================
# 1. Pydantic Models (Schemas for Data Validation)
# ==============================================================================

class Task(BaseModel):
    """Schema representing a complete Task object."""
    id: int
    title: str
    done: bool = False


class TaskCreate(BaseModel):
    """Schema for creating a new Task."""
    title: str = Field(..., description="Title of the task")


class TaskUpdate(BaseModel):
    """Schema for updating an existing Task."""
    title: Optional[str] = Field(None, description="New title of the task")
    done: Optional[bool] = Field(None, description="Completion status of the task")


# ==============================================================================
# 2. FastAPI Application Initialization & Swagger OpenAPI Metadata
# ==============================================================================

app = FastAPI(
    title="Task API",
    description="A beginner-friendly REST-style CRUD Task API built with Python and FastAPI.",
    version="1.0"
)

# ==============================================================================
# 3. In-Memory Data Store (Initial 3 Tasks)
# ==============================================================================

tasks_db: List[dict] = [
    {"id": 1, "title": "Learn FastAPI basics", "done": True},
    {"id": 2, "title": "Build a CRUD Task API", "done": False},
    {"id": 3, "title": "Test endpoints with Swagger UI", "done": False},
]


def get_next_id() -> int:
    """Helper function to calculate the next available task ID."""
    if not tasks_db:
        return 1
    return max(task["id"] for task in tasks_db) + 1


# ==============================================================================
# 4. API Endpoints
# ==============================================================================

@app.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="API Root Information",
    description="Returns general information about the API and available endpoints.",
    tags=["Root & Health"]
)
def get_root():
    """Return JSON describing the API."""
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get(
    "/health",
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Returns the health status of the API server.",
    tags=["Root & Health"]
)
def get_health():
    """Return API operational status."""
    return {
        "status": "ok"
    }


@app.get(
    "/tasks",
    response_model=List[Task],
    status_code=status.HTTP_200_OK,
    summary="Get All Tasks",
    description="Retrieve the complete list of all stored tasks.",
    tags=["Tasks"]
)
def get_all_tasks():
    """Return the complete list of tasks."""
    return tasks_db


@app.get(
    "/tasks/{id}",
    response_model=Task,
    status_code=status.HTTP_200_OK,
    summary="Get Task by ID",
    description="Retrieve a single task by its unique numeric ID.",
    tags=["Tasks"]
)
def get_task_by_id(id: int):
    """Return one task by ID or 404 if not found."""
    for task in tasks_db:
        if task["id"] == id:
            return task
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with ID {id} not found"
    )


@app.post(
    "/tasks",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
    summary="Create a New Task",
    description="Add a new task to the in-memory store. Next ID is auto-assigned and 'done' defaults to false.",
    tags=["Tasks"]
)
def create_task(task_input: TaskCreate):
    """Create a new task with validation."""
    # Check if title is missing, empty, or whitespace only
    if not task_input.title or not task_input.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Title is required and cannot be empty or whitespace only"
        )
    
    new_task = {
        "id": get_next_id(),
        "title": task_input.title.strip(),
        "done": False
    }
    
    tasks_db.append(new_task)
    return new_task


@app.put(
    "/tasks/{id}",
    response_model=Task,
    status_code=status.HTTP_200_OK,
    summary="Update Task by ID",
    description="Update the 'title' and/or 'done' status of an existing task by ID.",
    tags=["Tasks"]
)
def update_task(id: int, task_input: TaskUpdate):
    """Update an existing task's title or done status."""
    # Find target task
    target_task = None
    for task in tasks_db:
        if task["id"] == id:
            target_task = task
            break
            
    if not target_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {id} not found"
        )
    
    # Validate title if provided
    if task_input.title is not None:
        if not task_input.title.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Title cannot be empty or whitespace only"
            )
        target_task["title"] = task_input.title.strip()
        
    if task_input.done is not None:
        target_task["done"] = task_input.done
        
    return target_task


@app.delete(
    "/tasks/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Task by ID",
    description="Remove a task from the in-memory store by ID. Returns HTTP 204 with no body if successful.",
    tags=["Tasks"]
)
def delete_task(id: int):
    """Delete a task by ID."""
    for index, task in enumerate(tasks_db):
        if task["id"] == id:
            tasks_db.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task with ID {id} not found"
    )
