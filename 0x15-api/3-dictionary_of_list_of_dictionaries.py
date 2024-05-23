#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format.
"""

import json
import requests


def write_all_employees_todo_list_to_json():
    """returns information about his/her TODO and write it in a CSV file."""
    try:
        # Fetch all employee details
        users_url = "https://jsonplaceholder.typicode.com/users"
        users_response = requests.get(users_url)
        users_data = users_response.json()

        if users_response.status_code != 200 or not users_data:
            print("No employee data found.")
            return

        # Dictionary to hold all tasks for all employees
        all_employees_data = {}

        # Fetch TODO list for each employee
        for user in users_data:
            emp_id = user['id']
            employee_name = user['name']
            dom_name = "jsonplaceholder.typicode.com"

            todos_url = f"https://{dom_name}/todos?userId={emp_id}"
            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()

            if todos_response.status_code == 200 and todos_data:
                tasks_list = [{
                    "username": employee_name,
                    "task": task['title'],
                    "completed": task['completed']
                } for task in todos_data]

                all_employees_data[str(emp_id)] = tasks_list

        # Export data to JSON
        json_filename = "todo_all_employees.json"
        with open(json_filename, mode='w') as json_file:
            json.dump(all_employees_data, json_file, indent=4)

        print(f"Data exported to {json_filename}")

    except Exception as e:
        pass


if __name__ == "__main__":
    write_all_employees_todo_list_to_json()
