#!/usr/bin/python3
""" Test with jsonplaceholder API """

import json
import requests
import sys


def get_tasks(id):
    """ gets all tasks from an ID """
    """ Get the todos matching the UserId provided by argv """
    api_url = "https://jsonplaceholder.typicode.com"
    api = requests.get('{}/todos?userId={}'.format(api_url, id))
    todo_d = api.json()

    """ Need to get the matching users name with the ID from the post """
    api2 = requests.get('{}/users?id={}'.format(api_url, id))
    name = api2.json()

    """ All content is his ID so the first dict will work """
    name = name[0].get('username')

    task_list = []
    for task in todo_d:
        """ create a dict of each task and append it to the task list """
        full_task = {}
        full_task['username'] = name
        full_task['task'] = task.get('title')
        full_task["completed"] = task.get('completed')
        task_list.append(full_task)

    return task_list


if __name__ == "__main__":

    """ Get the todos matching the UserId provided by argv """
    api_url = "https://jsonplaceholder.typicode.com"
    api = requests.get('{}/todos'.format(api_url))
    todo_d = api.json()

    """ Get a list of all the userIDs in the API """
    id_list = []
    for task in todo_d:
        if task.get('userId') not in id_list:
            id_list.append(task.get('userId'))

    jdict = {}
    """ Get all the tasks for each ID and save them in a dict by id """
    for id in id_list:
        jdict[id] = get_tasks(id)

    """ Create a json object with the new dict and dump it into a json file """
    j_obj = json.dumps(jdict)
    with open('todo_all_employees.json', mode='w') as file:
        file.write(j_obj)
