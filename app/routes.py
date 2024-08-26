# app/routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

# Create a FastAPI router
router = APIRouter(
    prefix="/todos",  # Set a prefix for all routes in this router
    tags=["todos"],  # Set tags for Swagger UI documentation
    responses={404: {"description": "Not Found"}},  # Define common responses
)

# Define the Pydantic model for a TODO item


class Todo(BaseModel):
    id: str
    task: str


# In-memory storage for demonstration purposes
TODOS: Dict[str, Dict[str, str]] = {
    "todo1": {"task": "Build an API"},
    "todo2": {"task": "Write docs"},
    "todo3": {"task": "Test the app"},
}


@router.get("/{id}", response_model=Todo, summary="Fetch a given resource")
async def get_todo(id: str):
    """Fetch a given resource"""
    if id not in TODOS:
        raise HTTPException(status_code=404, detail=f"Todo {id} doesn't exist")
    return {"id": id, "task": TODOS[id]["task"]}


@router.delete("/{id}", status_code=204, summary="Delete a task given its identifier")
async def delete_todo(id: str):
    """Delete a task given its identifier"""
    if id not in TODOS:
        raise HTTPException(status_code=404, detail=f"Todo {id} doesn't exist")
    del TODOS[id]
    return {}
