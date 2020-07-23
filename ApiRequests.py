import requests

def launchGetRequest(url, parameters) :
    request = requests.get(url, parameters)
    data = request.json()
    return (data)

def launchPostRequest(url, body) :
    request = requests.post(url, json=body)
    print(request.headers)
    print(request.text)

