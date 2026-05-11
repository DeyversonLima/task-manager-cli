import json
from app.task_manager import add_task, list_tasks, complete_task

TEST_FILE = "data/tasks.json"


def setup_function():
    with open(TEST_FILE, "w") as f:
        json.dump([], f)


def test_add_task():
    add_task("Estudar")
    tasks = list_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Estudar"


def test_add_empty_task():
    try:
        add_task("")
    except ValueError:
        assert True
    else:
        assert False


def test_complete_task():
    add_task("Teste")
    complete_task(0)
    tasks = list_tasks()
    assert tasks[0]["done"] is True
