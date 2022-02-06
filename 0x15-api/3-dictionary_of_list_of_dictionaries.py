#!/usr/bin/python3
"""Export to-do list  information of employees to JSON format"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump({u.get('id'):[{
            'tasks': td.get('title'),
            'completed': td.get('completed'),
            'username': u.get('username')}
                                for td in requests.get(url + "todos",
                                                       params={"userId": u.get('id')}).json()]
                   for u in user}, jsonfile)
