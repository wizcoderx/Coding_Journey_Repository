'''
    Create a class `Task` with attributes `title`, `description`, and `completed` (a boolean). Implement methods to mark a task as completed and change the description. Then, create a class `TaskManager` that can hold multiple tasks. Add methods to add a task, remove a task, list all tasks, and show all completed tasks.
'''
class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    # Method to mark a task as completed
    def mark_completed(self):
        self.completed = True

    # Method to change the description
    def change_description(self, new_description):
        self.description = new_description


class TaskManager:
    def __init__(self):
        self.tasks = []  # List to hold multiple tasks

    # Method to add a task
    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        return f"The following task '{title}' has been added!"

    # Method to remove a task
    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return f"The task '{title}' has been removed!"
        return "Task not found!"

    # Method to list all tasks
    def list_tasks(self):
        if not self.tasks:
            return "No tasks available."
        return "\n".join(
            f"Title: {task.title}, Description: {task.description}, Completed: {task.completed}"
            for task in self.tasks
        )

    # Method to list all completed tasks
    def list_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.completed]
        if not completed_tasks:
            return "No tasks completed."
        return "\n".join(
            f"Title: {task.title}, Description: {task.description}" for task in completed_tasks
        )

# Creating TaskManager instance
task_manager = TaskManager()

# Adding tasks
print(task_manager.add_task("Task 1", "Description for task 1"))
print(task_manager.add_task("Task 2", "Description for task 2"))
print(task_manager.add_task("Task 3", "Description for task 3"))

# Listing all tasks
print("\nAll Tasks:")
print(task_manager.list_tasks())

# Marking a task as completed
task_manager.tasks[1].mark_completed()  # Mark "Task 2" as completed

# Listing all completed tasks
print("\nCompleted Tasks:")
print(task_manager.list_completed_tasks())

# Changing the description of a task
task_manager.tasks[0].change_description("Updated description for task 1")

# Removing a task
print("\nRemoving Task:")
print(task_manager.remove_task("Task 1"))

# Listing all tasks after removal
print("\nAll Tasks After Removal:")
print(task_manager.list_tasks())



