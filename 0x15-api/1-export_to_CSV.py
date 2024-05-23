#!/usr/bin/python3
"""
extend your Python script to export data in the CSV format.
"""

import csv
import requests
import sys


def write_employee_todo_list_to_csv(emp_id):
    """returns information about his/her TODO and write it in a CSV file."""
    try:
        user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
        user_response = requests.get(user_url)
        user_data = user_response.json()

        todourl = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
        todo_response = requests.get(todourl)
        todo_data = todo_response.json()

        csv_filename = f"{emp_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            fieldnames = ["USER_ID", "USERNAME",
                          "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for task in todo_data:
                writer.writerow({
                    "USER_ID": emp_id,
                    "USERNAME": user_data.get("username"),
                    "TASK_COMPLETED_STATUS": task['completed'],
                    "TASK_TITLE": task['title']
                })

        print(f"Data exported to {csv_filename}")

    except Exception as e:
        pass


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        write_employee_todo_list_to_csv(sys.argv[1])
