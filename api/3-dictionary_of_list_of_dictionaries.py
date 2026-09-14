#!/usr/bin/python3
"""Fetch all employees' TODO list data and export to JSON format."""

import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users and todos
    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    # Map user IDs to usernames
    user_dict = {user.get("id"): user.get("username") for user in users}

    # Aggregate tasks for all users
    all_tasks = {}
    for user_id, username in user_dict.items():
        all_tasks[str(user_id)] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in todos
            if task.get("userId") == user_id
        ]

    # Save aggregated data
    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(all_tasks, json_file)
