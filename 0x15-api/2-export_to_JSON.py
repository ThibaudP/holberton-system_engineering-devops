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

    taskList = []
    for task in todo:
        formattedTask = {"task": task['title'], "completed": task['completed'],
                         "username": user['username']}
        taskList.append(formattedTask)

    taskDict = {argv[1]: taskList}
    taskJSON = json.dumps(taskDict)

    with open("{:s}.json".format(argv[1]), "w") as file:
        file.write(taskJSON)


if __name__ == "__main__":
    main()
