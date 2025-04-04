from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Определение модели для задачи
class Task(BaseModel):
    id: int
    title: str

# Данные для примера
tasks = [
    Task(id=1, title="Task 1"),
    Task(id=2, title="Task 2")
]

# GET-запрос для получения всех задач
@app.get("/api/v1/tasks")
async def get_tasks():
    return tasks

# POST-запрос для добавления новой задачи
@app.post("/api/v1/tasks")
async def create_task(task: Task):
    tasks.append(task)
    return task

# PUT-запрос для обновления задачи
@app.put("/api/v1/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    task_to_update = next((t for t in tasks if t.id == task_id), None)
    if task_to_update is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task_to_update.title = task.title
    return task_to_update

# DELETE-запрос для удаления задачи
@app.delete("/api/v1/tasks/{task_id}")
async def delete_task(task_id: int):
    task_to_delete = next((t for t in tasks if t.id == task_id), None)
    if task_to_delete is None:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.remove(task_to_delete)
    return {"message": "Task deleted"}