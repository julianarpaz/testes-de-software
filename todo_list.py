class ToDoList:
    def __init__(self):
        self.max_tasks = 3
        self.completed_tasks = []
        self.tasks = []

    def get_tasks(self, task=None, index=None):
        if task is not None:
            if task in self.tasks:
                return task
            else:
                raise ValueError("Tarefa não encontrada na lista.")
        elif index is not None:
            try:
                return self.tasks[index]
            except IndexError:
                raise IndexError("Índice fora dos limites da lista.")
        else:
            return self.tasks
        
    def is_task_completed(self, task):
        return task in self.tasks and task.startswith("DONE")
    
    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not self.is_task_completed(task)]
        
    def add_task(self, task):
        self.clear_completed_tasks()
        if(len(self.tasks) < self.max_tasks):
            if(task not in self.tasks):
                self.tasks.append(task)
            else:
                raise ValueError("Task já está cadastrada.")
        else:
            raise ValueError("Limite de 3 tasks simultâneas atingido.")

    def remove_task(self, task=None, index=None):
        if task is not None:
            if task in self.tasks:
                self.tasks.remove(task)
            else:
                raise ValueError("Tarefa não encontrada na lista.")
        elif index is not None:
            try:
                self.tasks.pop(index)
            except IndexError:
                raise IndexError("Índice fora dos limites da lista.")
        else:
            raise ValueError("Especifique a tarefa ou o índice a ser removido.")

    def get_task_count(self):
        total_length = len(self.tasks)
        done = 0
        for task in self.tasks:
            if(task in self.tasks and task.startswith("DONE")):
                done = done + 1
        return total_length - done

    def complete_task(self, task):
        if task in self.tasks and not self.is_task_completed(task):
            self.tasks[self.tasks.index(task)] = "DONE - " + task
