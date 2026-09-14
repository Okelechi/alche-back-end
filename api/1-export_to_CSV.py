#!/usr/bin/python3
"""Export a given employee's TODO list data to CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(base_url + "users/{}".format(employee_id)).json()
    todos = requests.get(
        base_url + "todos", params={"userId": employee_id}).json()

    username = user.get("username")

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title"),
            ])
