import requests
import os


CONFIG_ID = os.environ['CONFIG_ID']
CONFIG_KEY = os.environ['CONFIG_KEY']


def gettoken(refresh_token: str) -> dict:
    '''返回字典包含 refresh_token, access_token'''
    
    url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CONFIG_ID,
        'client_secret': CONFIG_KEY,
        'redirect_uri': 'http://localhost:53682/'
    }
    
    return requests.post(url=url, data=data, headers=headers).json()
    

if __name__ == "__main__":
    with open('refresh.txt', 'r') as f:
        token = gettoken(f.read())
    
    with open('refresh.txt', 'w') as f:
        f.write(token['refresh_token'])
