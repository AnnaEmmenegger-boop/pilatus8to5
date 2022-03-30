#!/usr/bin/python3
import requests
from requests.exceptions import HTTPError
import subprocess
import time
import os

run = True
list = []


def whatever():
    try:
        response = requests.get("https://np.swissradioplayer.ch/qp/v4/events/?rpId=113")
        response.raise_for_status()

        jsonResponse = response.json()

        name = ""
        artist = ""

        try:
            name = jsonResponse["results"]["now"]["name"]
        except:
            name = jsonResponse["results"]["previous"][0]["name"]

        try:
            artist = jsonResponse["results"]["now"]["artistName"]
        except:
            artist = jsonResponse["results"]["previous"][0]["artistName"]

        return [str(name), str(artist)]


    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

while run:
    element = whatever()
    if element in list:
        if list.index(element) < len(list)-2:
            print(element)
            print("0848 20 10 20")
            os.system('mplayer song.mp3')
            run = False
    else:
        print(element)
        list.append(element)
time.sleep(5)
