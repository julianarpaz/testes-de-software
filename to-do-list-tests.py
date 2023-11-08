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
    assert str(exception_info.value) == "Task não encontrada na lista."

def test_get_all_tasks():

    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")
    to_do_list.add_task("Task 3")

    tasks = to_do_list.get_tasks()
    assert tasks == ["Task 1", "Task 2", "Task 3"]

def test_add_task_not_duplicated():
    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    with pytest.raises(ValueError) as exception_info:
        to_do_list.add_task("Task 1")
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

    to_do_list.add_task("DONE - Task 1")
    to_do_list.add_task("DONE - Task 2")
    to_do_list.add_task("Task 3")

    assert not any(task.startswith("DONE") for task in to_do_list.get_tasks())
    assert "Task 3" in to_do_list.get_tasks()

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

def test_remove_task_per_task_invalid_task():
    with pytest.raises(ValueError) as exception_info:
        to_do_list = ToDoList()
        to_do_list.add_task("Buy groceries")
        to_do_list.remove_task(task="Buy clothes")
        assert exception_info.type == ValueError
        assert str(exception_info.value) == "Task não encontrada na lista."

def test_remove_task_per_task():
    to_do_list = ToDoList()
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")
    to_do_list.add_task("Task 3")

    to_do_list.remove_task(task="Task 2")
    assert to_do_list.get_tasks() == ["Task 1", "Task 3"]

def test_remove_task_per_index_invalid_index():
    with pytest.raises(IndexError) as exception_info:
        to_do_list = ToDoList()
        to_do_list.add_task("Buy groceries")
        to_do_list.remove_task(index=1)
        assert exception_info.type == IndexError
        assert str(exception_info.value) == "Índice fora dos limites da lista."

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

def test_update_task_order():
    
    to_do_list = ToDoList()
    
    to_do_list.add_task("Tarefa 1")
    to_do_list.add_task("Tarefa 2")
    to_do_list.add_task("Tarefa 3")

    to_do_list.update_task(new_order=["Tarefa 2", "Tarefa 3", "Tarefa 1"])

    
    tasks = to_do_list.get_tasks()
    assert tasks == ["Tarefa 2", "Tarefa 3", "Tarefa 1"]

def test_update_task_with_update_task_name():
    to_do_list = ToDoList()
    
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")

    update_task_name = ("Task 1", "Task 1 Atualizada")
    to_do_list.update_task(update_task_name=update_task_name)

    tasks = to_do_list.get_tasks()
    assert "Task 1 Atualizada" in tasks
    assert "Task 1" not in tasks

def test_update_task_with_both_parameters():
    to_do_list = ToDoList()
    
    to_do_list.add_task("Task 1")
    to_do_list.add_task("Task 2")
    to_do_list.add_task("Task 3")

    new_order = ["Task 2", "Task 3", "Task 1"]
    update_task_name = ("Task 2", "Task 2 Atualizada")
    to_do_list.update_task(new_order=new_order, update_task_name=update_task_name)

    tasks = to_do_list.get_tasks()
    assert tasks == new_order
    assert "Task 2 Atualizada" in tasks
    assert "Task 2" not in tasks
