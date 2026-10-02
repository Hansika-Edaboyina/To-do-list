class Task:
    def __init__(self, description, priority="Medium"):
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def mark_pending(self):
        self.completed = False

    def edit_task(self, new_description):
        self.description = new_description

    def display_task(self, task_number):
        status = "Completed" if self.completed else "Pending"

        print(
            f"{task_number}. {self.description} "
            f"| Priority: {self.priority} "
            f"| Status: {status}"
        )


class TodoList:

    def __init__(self):
        self.tasks = []

    

    def add_task(self):
        description = input("Enter task description: ").strip()

        if description == "":
            print("Task description cannot be empty.")
            return

        print("\nSelect Priority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        priority_choice = input("Enter priority: ")

        if priority_choice == "1":
            priority = "High"
        elif priority_choice == "2":
            priority = "Medium"
        elif priority_choice == "3":
            priority = "Low"
        else:
            print("Invalid priority. Setting priority to Medium.")
            priority = "Medium"

        new_task = Task(description, priority)
        self.tasks.append(new_task)

        print("Task added successfully.")

    

    def view_tasks(self):

        if len(self.tasks) == 0:
            print("\nNo tasks available.")
            return

        print("\n========== YOUR TASKS ==========")

        for index, task in enumerate(self.tasks, start=1):
            task.display_task(index)

        print("================================")

   
    def complete_task(self):

        if len(self.tasks) == 0:
            print("No tasks available.")
            return

        self.view_tasks()

        try:
            task_number = int(
                input("\nEnter task number to mark as completed: ")
            )

            if 1 <= task_number <= len(self.tasks):

                task = self.tasks[task_number - 1]

                if task.completed:
                    print("Task is already completed.")
                else:
                    task.mark_completed()
                    print("Task marked as completed.")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

  
    def mark_pending(self):

        if len(self.tasks) == 0:
            print("No tasks available.")
            return

        self.view_tasks()

        try:
            task_number = int(
                input("\nEnter task number to mark as pending: ")
            )

            if 1 <= task_number <= len(self.tasks):

                self.tasks[task_number - 1].mark_pending()

                print("Task marked as pending.")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    

    def delete_task(self):

        if len(self.tasks) == 0:
            print("No tasks available.")
            return

        self.view_tasks()

        try:
            task_number = int(
                input("\nEnter task number to delete: ")
            )

            if 1 <= task_number <= len(self.tasks):

                deleted_task = self.tasks.pop(task_number - 1)

                print(
                    f"Task '{deleted_task.description}' "
                    f"deleted successfully."
                )

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

   

    def edit_task(self):

        if len(self.tasks) == 0:
            print("No tasks available.")
            return

        self.view_tasks()

        try:
            task_number = int(
                input("\nEnter task number to edit: ")
            )

            if 1 <= task_number <= len(self.tasks):

                new_description = input(
                    "Enter new task description: "
                ).strip()

                if new_description == "":
                    print("Task description cannot be empty.")
                    return

                self.tasks[task_number - 1].edit_task(
                    new_description
                )

                print("Task updated successfully.")

            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

    

    def search_task(self):

        if len(self.tasks) == 0:
            print("No tasks available.")
            return

        keyword = input(
            "Enter keyword to search: "
        ).strip().lower()

        found = False

       
        for index, task in enumerate(self.tasks, start=1):

            if keyword in task.description.lower():

                task.display_task(index)
                found = True

        if not found:
            print("No matching tasks found.")

       

    def show_statistics(self):

        total = len(self.tasks)

        completed = 0
        pending = 0

        for task in self.tasks:

            if task.completed:
                completed += 1
            else:
                pending += 1

       
        print(f"Total Tasks     : {total}")
        print(f"Completed Tasks : {completed}")
        print(f"Pending Tasks   : {pending}")

        if total > 0:
            percentage = (completed / total) * 100
            print(f"Completion Rate : {percentage:.2f}%")
        else:
            print("Completion Rate : 0%")

       
    def clear_tasks(self):

        if len(self.tasks) == 0:
            print("No tasks available.")
            return

        confirmation = input(
            "Are you sure you want to delete ALL tasks? (yes/no): "
        ).lower()

        if confirmation == "yes":

            self.tasks.clear()

            print("All tasks deleted successfully.")

        else:
            print("Operation cancelled.")


    def menu(self):

        while True:

            
            print("       TO-DO LIST APPLICATION")
           
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Mark Task as Pending")
            print("5. Edit Task")
            print("6. Delete Task")
            print("7. Search Task")
            print("8. Task Statistics")
            print("9. Clear All Tasks")
            print("10. Exit")

            

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_task()

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.complete_task()

            elif choice == "4":
                self.mark_pending()

            elif choice == "5":
                self.edit_task()

            elif choice == "6":
                self.delete_task()

            elif choice == "7":
                self.search_task()

            elif choice == "8":
                self.show_statistics()

            elif choice == "9":
                self.clear_tasks()

            elif choice == "10":
                print("\nThank you for using the To-Do List Application!")
                break

            else:
                print("Invalid choice. Please try again.")


todo = TodoList()

todo.menu()
