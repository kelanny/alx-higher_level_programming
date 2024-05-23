#!/usr/bin/python3

"""uses https://jsonplaceholder.typicode.com REST API, for a given employee ID
    - returns information about his/her TODO list progress.
"""

import requests
import sys


def get_employee_todo_progress(emp_id):
    try:
        user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
        user_response = requests.get(user_url)
        user_data = user_response.json()

        if user_response.status_code != 200 or not user_data:
            print(f"Employee with ID {emp_id} not found.")
            return

        emp_name = user_data['name']

        url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
        todos_response = requests.get(url)
        todos_data = todos_response.json()

        if todos_response.status_code != 200 or not todos_data:
            print(f"No TODO list found for employee ID {emp_id}.")
            return

        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task['completed']]
        no_tasks_done = len(done_tasks)
        msg = "Employee {} is done with tasks({}/{}):".format(
            emp_name, no_tasks_done, total_tasks
        )
        print(msg)
        for task in done_tasks:
            print(f"\t {task['title']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            emp_id = int(sys.argv[1])
            get_employee_todo_progress(emp_id)
        except ValueError:
            print("Please provide a valid integer for employee ID.")
