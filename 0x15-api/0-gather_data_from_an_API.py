#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 2:
        n = argv[1]

        userUrl = "https://jsonplaceholder.typicode.com/users/{}".format(n)
        todoUrl = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            n)

        userReq = requests.get(userUrl)
        user = userReq.json()
        todoReq = requests.get(todoUrl)
        todo = todoReq.json()

        completed = []
        for task in todo:
            if task.get('completed'):
                completed.append(task)

        print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
                                                             len(completed),
                                                             len(todo)))
        for task in completed:
            print("\t {}".format(task.get('title')))
