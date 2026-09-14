#!/usr/bin/python3
"""Fetch employee TODO list data and export to JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user username
    user_res = requests.get("{}/users/{}".format(base_url, user_id))
    username = user_res.json().get("username")

    # Fetch user tasks
    todos_res = requests.get(
        "{}/todos".format(base_url), params={"userId": user_id}
    )
    todos = todos_res.json()

    # Format JSON structure
    user_tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }
        for task in todos
    ]

    json_data = {user_id: user_tasks}

    # Save to file
    filename = "{}.json".format(user_id)
    with open(filename, mode="w") as json_file:
        json.dump(json_data, json_file)
