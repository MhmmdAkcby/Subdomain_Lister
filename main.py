from unittest import makeSuite

import requests

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_input = "google.com"

with open("subdomainlist.txt","r") as subdomin_list:
    for word in subdomin_list:
        word = word.strip()
        url = "https://"+word + "."+ target_input
        response = make_request(url)
        if response:
            print("Found subdomain ---> " + url)