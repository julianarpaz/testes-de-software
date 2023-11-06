class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_task_count(self):
        return len(self.tasks)

    def is_task_completed(self, task):
        return task in self.tasks and task.startswith("DONE")

    def complete_task(self, task):
        if task in self.tasks and not self.is_task_completed(task):
            self.tasks[self.tasks.index(task)] = "DONE - " + task

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not self.is_task_completed(task)]
