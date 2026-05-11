import json
import os

TASKS_FILE = "data/tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(title):
    if not title.strip():
        raise ValueError("A tarefa não pode ser vazia.")

    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)


def list_tasks():
    return load_tasks()


def complete_task(index):
    tasks = load_tasks()
    if index < 0 or index >= len(tasks):
        raise IndexError("Índice inválido.")

    tasks[index]["done"] = True
    save_tasks(tasks)


def remove_task(index):
    tasks = load_tasks()
    if index < 0 or index >= len(tasks):
        raise IndexError("Índice inválido.")

    tasks.pop(index)
    save_tasks(tasks)
