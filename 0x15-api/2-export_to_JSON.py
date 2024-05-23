#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format.
"""

import json
import requests
import sys


def write_employee_todo_list_to_json(emp_id):
    """returns information about his/her TODO and write it in a CSV file."""
    try:
        user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
        user_response = requests.get(user_url)
        user_data = user_response.json()

        todourl = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
        todo_response = requests.get(todourl)
        todo_data = todo_response.json()

        emp_name = user_data.get("name")

        tasks_list = [{
            "task": task['title'],
            "completed": task['completed'],
            "username": emp_name
        } for task in todo_data]

        json_data = {
            str(emp_id): tasks_list
        }

        json_filename = f"{emp_id}.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Data exported to {json_filename}")

    except Exception as e:
        pass


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        write_employee_todo_list_to_json(sys.argv[1])
