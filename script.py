import requests
import json
import pandas as pd
import configparser


config = configparser.ConfigParser()
config.read('credentials.config')
key = config.get('ClientKey', 'key')
secret = config.get('ClientKey', 'secret')
Workspace = input("Enter Workspace name here:")

data = { 'grant_type': 'client_credentials'}

response = requests.post('https://bitbucket.org/site/oauth2/access_token', data=data, auth=(key, secret))

access_token = response.json()['access_token']
access_token=str(access_token)
print(access_token)

api_url = 'https://api.bitbucket.org/2.0/repositories/Rahul_sharma_12345/reposit_1/access'
username = 'Rahul_sharma_12Ra345'
password = 'ATBBQkHMgDFZcLQHuMD8mG4jueCN14A73F72'

headers = {
    'Content-Type': 'application/json'
}
data = {
    'permission': 'write',
    'user': {
        'username': 'Xyz_beta'
    }
}


response = requests.post(api_url, auth=(username, password), headers=headers, data=json.dumps(data))

print(response)
if response.status_code == 200:
    print('User added to repository access list')
else:
    print('Error adding user to repository access list')
