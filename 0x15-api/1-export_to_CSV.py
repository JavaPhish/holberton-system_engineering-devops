#!/usr/bin/python3
""" Test with jsonplaceholder API """

import requests
import json
import sys
import csv


if __name__ == "__main__":

    """ Get the todos matching the UserId provided by argv """
    api_url = "https://jsonplaceholder.typicode.com"
    api = requests.get('{}/todos?userId={}'.format(api_url, sys.argv[1]))
    todo_d = json.loads(api.content)

    """ Need to get the matching users name with the ID from the post """
    api2 = requests.get('{}/users?id={}'.format(api_url, sys.argv[1]))
    name = json.loads(api2.content)

    """ All content is his ID so the first dict will work """
    name = name[0].get('username')

    """ Now we have the name, and the todos list """

    """ Using our data, write each line of a CSV file to contain a task """
    with open('USER_ID.csv', mode='w') as file:
        for task in todo_d:
            csv_w = csv.writer(file,
                               delimiter=',',
                               quotechar='"',
                               quoting=csv.QUOTE_ALL)

            csv_w.writerow([sys.argv[1],
                           name,
                           task.get('completed'),
                           task.get('title')])
