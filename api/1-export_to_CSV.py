#!/usr/bin/python3
"""Fetch employee TODO list data and export to CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_res = requests.get("{}/users/{}".format(base_url, user_id))
    username = user_res.json().get("username")

    # Fetch TODO tasks
    todos_res = requests.get(
        "{}/todos".format(base_url), params={"userId": user_id}
    )
    todos = todos_res.json()

    # Write to CSV with double quotes around all fields
    filename = "{}.csv".format(user_id)
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow(
                [
                    user_id,
                    username,
                    task.get("completed"),
                    task.get("title"),
                ]
            )
