import pytest
from todo_list import ToDoList

def test_get_tasks_per_index():
    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")
    to_do_list.add_task("Task 3")

    task = to_do_list.get_tasks(index=1)
    assert task == "Task 2"

def test_get_tasks_invalid_index():

    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")

    with pytest.raises(IndexError) as exception_info:
        to_do_list.get_tasks(index=10)
    assert str(exception_info.value) == "Índice fora dos limites da lista."

def test_get_tasks_per_task():
    
    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")
    to_do_list.add_task("Task 3")

    task = to_do_list.get_tasks(task="Task 3")
    assert task == "Task 3"

def test_get_tasks_task_not_found():

    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")

    with pytest.raises(ValueError) as exception_info:
        to_do_list.get_tasks(task="Task 3")
    assert str(exception_info.value) == "Tarefa não encontrada na lista."

def test_get_all_tasks():

    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")
    to_do_list.add_task("Task 3")

    tasks = to_do_list.get_tasks()
    assert tasks == ["Task 1", "Task 2", "Task 3"]

def test_add_task_not_duplicated():
    with pytest.raises(ValueError):
        to_do_list = ToDoList()
        to_do_list.add_task("Buy groceries")
        with pytest.raises(ValueError) as exception_info:
            to_do_list.add_task("Buy groceries")
        assert str(exception_info.value) == "Task já está cadastrada."

def test_add_task_max_tasks_reached():
    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")
    to_do_list.add_task("Task 3")

    with pytest.raises(ValueError) as excecao_info:
        to_do_list.add_task("Task 4")

    assert str(excecao_info.value) == "Limite de 3 tasks simultâneas atingido."

def test_add_task_with_clearing_completed_tasks():
    to_do_list = ToDoList()

    to_do_list.add_task("DONE - Tarefa 1")
    to_do_list.add_task("DONE - Tarefa 2")
    to_do_list.add_task("Tarefa 3")

    assert not any(task.startswith("DONE") for task in to_do_list.get_tasks())
    assert "Tarefa 3" in to_do_list.get_tasks()

def test_add_task_not_found():
    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 3")

    with pytest.raises(ValueError) as exception_info:
        to_do_list.remove_task(task="Task 2")
        assert str(exception_info.value) == "Task não encontrada na lista."

def test_add_task_invalid_index():
    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")
    to_do_list.add_task("Task 3")

    with pytest.raises(IndexError) as exception_info:
        to_do_list.remove_task(index=10)
        assert str(exception_info.value) == "Índice fora dos limites da lista."

def test_remove_task_per_task():
    with pytest.raises(ValueError) as exception_info:
        to_do_list = ToDoList()
        to_do_list.add_task("Buy groceries")
        to_do_list.remove_task(task="Buy clothes")
        assert exception_info.type == ValueError
        assert str(exception_info.value) == "Tarefa não encontrada na lista."

def test_remove_task_per_index():
    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")
    to_do_list.add_task("Task 3")

    to_do_list.remove_task(index=1)
    assert to_do_list.get_tasks() == ["Task 1", "Task 3"]

def test_complete_task():
    to_do_list = ToDoList()
    to_do_list.add_task("Buy groceries")
    to_do_list.complete_task("Buy groceries")
    to_do_list.complete_task("Buy groceries")
    assert to_do_list.is_task_completed("DONE - Buy groceries")

def test_clear_completed_tasks():
    to_do_list = ToDoList()
    to_do_list.add_task("Buy groceries")
    to_do_list.complete_task("Buy groceries")
    to_do_list.clear_completed_tasks()
    assert to_do_list.get_task_count() == 0

def test_get_task_count():
    to_do_list = ToDoList()
    to_do_list.add_task("Buy groceries")
    to_do_list.complete_task("Buy groceries")
    to_do_list.add_task("Buy clothes")
    assert to_do_list.get_task_count() == 1
