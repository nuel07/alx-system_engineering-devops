#!/usr/bin/python3
"""Returns information about TODO list of employee"""

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    tdlst = requests.get(url + 'tdlst', params={"userId":user_id}).json()
    complete = [tsk.get("title") for tsk in tdlst if tsk.get("completed") is True]
    print("Employee {} is done with tasks {}/{}".format(user.get("name"),
                                                        len(complete), len(tdlst)))
    [print("\t {}".format(dne)) for dne in complete]
