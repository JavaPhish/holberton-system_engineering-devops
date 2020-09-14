#!/usr/bin/python3
""" Test with jsonplaceholder API """

import json
import requests
from sys import argv


if __name__ == "__main__":

    """ Get the todos matching the UserId provided by argv """
    api_url = "https://jsonplaceholder.typicode.com"
    api = requests.get('{}/todos?userId={}'.format(api_url, argv[1]))
    todo_d = api.json()

    task_total = 0
    task_completed = 0

    for task in todo_d:
        """ Count all the tasks and tasks completed (list of tasks) """
        task_total += 1

        if task.get('completed') is True:
            task_completed += 1

    """ Need to get the matching users name with the ID from the post """
    api2 = requests.get('{}/users/{}'.format(api_url, argv[1]))
    name = api2.json()
    """ All content is his ID so the first dict will work """
    uname = name.get('name')

    """ First print string :) """
    print('Employee {} is done with tasks({}/{}):'.format(uname,
                                                          task_completed,
                                                          task_total))

    """ print all the tasks (Just gonna re use todo_data) """
    for task in todo_d:
        if task['completed'] is True:
            print(' \t{}'.format(task.get('title')))
