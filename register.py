import requests

data = {'token': 'f1f678e201bd75e55acaa749f3173a25', 'github':'https://github.com/skeledrew/code2040'}
resp = requests.post('http://challenge.code2040.org/api/register', data=data)
print('Received: '+ resp.text)
