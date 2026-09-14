#!/usr/bin/python3
"""Export a given employee's TODO list data to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(
        base_url + "todos", params={"userId": employee_id}).json()

    username = user.get("username")
    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        for task in todos
    ]

    data = {employee_id: tasks}

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump(data, json_file)
