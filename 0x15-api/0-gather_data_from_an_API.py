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

        todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        completed_tasks = []
        for task in todo_data:
            if task.get("completed"):
                completed_tasks.append(task.get("title"))

        print(f"Employee {} is done with tasks({}/{}):".format(
            user_data.get("name"), len(completed_tasks), len(todo_data)))

        for task in completed_tasks:
            print("\t {}".format(task))

    except Exception as e:
        pass

