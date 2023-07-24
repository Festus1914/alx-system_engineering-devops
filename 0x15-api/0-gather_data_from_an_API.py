#!/usr/bin/python3
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def get_employee_todo_progress(employee_id):
    # Fetching the employee information using the provided REST API
    response = requests.get(f"{API_URL}/{employee_id}")
    if response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    employee_data = response.json()
    employee_name = employee_data['name']

    # Fetching the TODO list for the given employee
    response = requests.get(f"{API_URL}/{employee_id}/todos")
    if response.status_code != 200:
        print(f"Error: Could not retrieve TODO list for employee {employee_name}.")
        return

    todo_list = response.json()

    # Counting completed tasks and total tasks
    num_completed_tasks = sum(1 for task in todo_list if task['completed'])
    total_tasks = len(todo_list)

    # Displaying the progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")

    # Displaying the completed task titles
    for task in todo_list:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python todo_progress.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
