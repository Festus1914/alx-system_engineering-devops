#!/usr/bin/python3
"""
Uses READ API for a given employee ID,
Returns information about the employee TODO list
progress
"""
import requests
from sys import argv


if __name__ == "__main__":
    """prevents from executing when imported"""
    all_users = requests.get("https://jsonplaceholder.typicode.com/users")
    for user in all_users.json():
        if user.get('id') == int(argv[1]):
            Username = (user.get("name"))
            break
    Completed = 0
    Total = 0
    Title = []
    tasks = requests.get("http://jsonplaceholder.typicode.com/todos")
    for task in tasks.json():
        if task.get("userId") == int(argv[1]):
            Total += 1
            if task.get("completed") is True:
                Completed += 1
                Title.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(Username, Completed,
                                                          Total))
    for task in Title:
        print("\t {}".format(task))
