#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv


def main():
    """main function"""
    if len(argv) == 2:

        n = argv[1]

        userUrl = "https://jsonplaceholder.typicode.com/users/{}".format(n)
        todoUrl = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            n)

        userReq = requests.get(userUrl)
        user = json.loads(userReq.text)
        todoReq = requests.get(todoUrl)
        todo = json.loads(todoReq.text)

        completed = []
        for task in todo:
            if task.get('completed'):
                completed.append(task)

        print("Employee {} is done with tasks({}/{})".format(user.get('name'),
                                                             len(completed),
                                                             len(todo)))
        for task in completed:
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    main()
