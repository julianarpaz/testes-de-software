import unittest

from todo_list import ToDoList


class TestToDoList(unittest.TestCase):

    def test_add_task(self):
        to_do_list = ToDoList()
        to_do_list.add_task("Buy groceries")
        self.assertEqual(to_do_list.get_task_count(), 1)

    def test_remove_task(self):
        to_do_list = ToDoList()
        to_do_list.add_task("Buy groceries")
        to_do_list.remove_task("Buy groceries")
        self.assertEqual(to_do_list.get_task_count(), 0)

    def test_complete_task(self):
        to_do_list = ToDoList()
        to_do_list.add_task("Buy groceries")
        to_do_list.complete_task("Buy groceries")
        self.assertTrue(to_do_list.is_task_completed("DONE - Buy groceries"))

    def test_clear_completed_tasks(self):
        to_do_list = ToDoList()
        to_do_list.add_task("Buy groceries")
        to_do_list.complete_task("Buy groceries")
        to_do_list.clear_completed_tasks()
        self.assertEqual(to_do_list.get_task_count(), 0)

    # Outros cenários de teste...

if __name__ == "__main__":
    unittest.main()
