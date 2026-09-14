#!/usr/bin/python3
"""Fetch and display employee TODO list progress from JSONPlaceholder API."""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_res = requests.get("{}/users/{}".format(base_url, employee_id))
    user = user_res.json()
    employee_name = user.get("name")

    # Fetch TODO list for the employee
    todos_res = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id}
    )
    todos = todos_res.json()

    # Calculate completed vs total tasks
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    done_tasks_count = len(completed_tasks)

    # Output details
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, done_tasks_count, total_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
