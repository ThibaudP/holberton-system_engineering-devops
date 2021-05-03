#!/usr/bin/python3
"""Gather data from an API"""
import csv
import json
import requests
from sys import argv


def main():
    """main function"""
    if len(argv) < 2:
        return

    userUrl = "https://jsonplaceholder.typicode.com/users/{:s}".format(argv[1])
    todoUrl = "https://jsonplaceholder.typicode.com/users/{:s}/todos".format(
        argv[1])

    userReq = requests.get(userUrl)
    user = json.loads(userReq.text)
    todoReq = requests.get(todoUrl)
    todo = json.loads(todoReq.text)

    with open("{:s}.csv".format(argv[1]), "w") as file:
        writer = csv.writer(file)
        for task in todo:
            writer.writerow(
                [argv[1], user['name'], task['completed'], task['title']])


if __name__ == "__main__":
    main()
