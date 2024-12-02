# To-Do List Application

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added to the list.")

# Function to view all pending tasks
def view_tasks():
    print("Pending tasks:")
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i + 1}. {task['task']}")

# Function to mark a task as completed
def complete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task '{tasks[task_number - 1]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

# Function to delete a task
def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' deleted from the list.")
    else:
        print("Invalid task number.")

# Main loop
while True:
    print("\nTo-Do List Application")
    print("1. Add a task")
    print("2. View all pending tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_number = int(input("Enter the task number to mark as completed: "))
        complete_task(task_number)
    elif choice == "4":
        task_number = int(input("Enter the task number to delete: "))
        delete_task(task_number)
    elif choice == "5":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
