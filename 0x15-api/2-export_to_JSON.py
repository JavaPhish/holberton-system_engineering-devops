#!/usr/bin/python3
""" Test with jsonplaceholder API """

import json
import requests
from sys import argv


if __name__ == "__main__":

    """ Get the todos matching the UserId provided by argv """
    api_url = "https://jsonplaceholder.typicode.com"
    api = requests.get('{}/todos?userId={}'.format(api_url, sys.argv[1]))
    todo_d = api.json()

    """ Need to get the matching users name with the ID from the post """
    api2 = requests.get('{}/users?id={}'.format(api_url, sys.argv[1]))
    name = api2.json()

    """ All content is his ID so the first dict will work """
    name = name[0].get('username')

    """ Generate our json object to dump into USER_ID.json """
    task_list = []
    for task in todo_d:
        """ create a dict of each task and append it to the task list """
        full_task = {}
        full_task['task'] = task.get('title')
        full_task["completed"] = task.get('completed')
        full_task['username'] = name
        task_list.append(full_task)

    """ Add that list to a dict """
    jdict = {}
    jdict['{}'.format(sys.argv[1])] = task_list

    """ Create a json object with the new dict and dump it into a json file """
    j_obj = json.dumps(jdict)
    with open('{}.json'.format(argv[1]), mode='w') as file:
        file.write(j_obj)
