from typing import List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str
    # TODO: Add Pydantic validation to reject empty titles.
    completed: bool = False


class Task(TaskInput):
    id: int


# In-memory storage; tasks are reset whenever the server restarts.
tasks: List[Task] = []
next_task_id = 1


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Find and return the task, or raise HTTPException with status 404.
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput):
    global next_task_id
    # TODO: Create a task with a unique ID, store it, and return it.
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput):
    # TODO: Update the task, or raise HTTPException with status 404.
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # TODO: Delete the task, or raise HTTPException with status 404.
    pass
