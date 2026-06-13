class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def display_task(self, task_number):
        status = "Completed" if self.completed else "Pending"
        print(f"{task_number}. {self.description} - {status}")


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        description = input("Enter task description: ")

        if description.strip() == "":
            print("Task description cannot be empty.")
            return

        new_task = Task(description)
        self.tasks.append(new_task)

        print("Task added successfully.")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks available.")
            return

        print("\nYour Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            task.display_task(index)

    def complete_task(self):
        if len(self.tasks) == 0:
            print("No tasks available to complete.")
            return

        self.view_tasks()

        try:
            task_number = int(input("\nEnter task number to mark as completed: "))

            if 1 <= task_number <= len(self.tasks):
                self.tasks[task_number - 1].mark_completed()
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    def menu(self):
        while True:
            print("\n===== TO-DO LIST MENU =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.complete_task()

            elif choice == "4":
                print("Exiting To-Do List Application.")
                break

            else:
                print("Invalid choice. Please try again.")


todo = TodoList()
todo.menu()