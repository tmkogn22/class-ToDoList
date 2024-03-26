class ToDoList:
        def __init__(self, tasks):
            self.tasks = tasks

        def add_task(self):
            task = input("What task do you want to add? Type: ")
            self.tasks.append(task)
            print("Now your list looks like this:", self.tasks)

        def remove_task(self):
            print("What task do you want to remove? You can remove tasks with its index. for example, last task "
                  "has index "
                  "-1, penultimate has index -2 and so on. First task has index 0, second task is 1 and so on.")
            task_to_remove = int(input("Type your index: "))
            self.tasks.pop(task_to_remove)
            print("Now your list looks like this: ", self.tasks)

        def show_list(self):
            print(self.tasks)


todolist = ToDoList(tasks=list())

todolist.add_task()
todolist.remove_task()
todolist.show_list()
