import os
import json
from datetime import datetime

# Initialize an empty list to store the tasks
tasks = []

# Function to add a task to the list
def add_task(task, due_date=None):
    task_info = {
        "task": task,
        "due_date": due_date,
        "completed": False,
    }
    tasks.append(task_info)
    print(f"Task '{task}' has been added to the to-do list.")

# Function to view the tasks in the list
def view_tasks():
    if not tasks:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task_info in enumerate(tasks, start=1):
            status = "Completed" if task_info["completed"] else "Pending"
            due_date = task_info["due_date"] if task_info["due_date"] else "No due date"
            print(f"{i}. {task_info['task']} ({due_date}) - {status}")

# Function to mark a task as completed
def complete_task(task_number):
    if task_number >= 1 and task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task '{tasks[task_number - 1]['task']}' has been marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function to remove a task from the list
def remove_task(task_number):
    if task_number >= 1 and task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' has been removed from the to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function to save tasks to a file
def save_tasks(filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file)
    print(f"Tasks have been saved to {filename}.")

# Function to load tasks from a file
def load_tasks(filename="tasks.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            loaded_tasks = json.load(file)
            tasks.extend(loaded_tasks)
        print(f"Tasks have been loaded from {filename}.")
    else:
        print(f"The file {filename} does not exist.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Complete a task")
    print("4. Remove a task")
    print("5. Save tasks to file")
    print("6. Load tasks from file")
    print("7. Quit")
    
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")
    
    if choice == '1':
        task = input("Enter the task: ")
        due_date_str = input("Enter due date (YYYY-MM-DD) or leave blank: ")
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
        add_task(task, due_date)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        complete_task(task_number)
    elif choice == '4':
        view_tasks()
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    elif choice == '5':
        save_filename = input("Enter the filename to save tasks (default: tasks.json): ")
        save_tasks(save_filename)
    elif choice == '6':
        load_filename = input("Enter the filename to load tasks (default: tasks.json): ")
        load_tasks(load_filename)
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")