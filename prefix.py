import requests
import json

verify = {'token': 'f1f678e201bd75e55acaa749f3173a25'}
resp = requests.post('http://challenge.code2040.org/api/prefix', data=verify)
print('Received: '+ resp.text)
dic = json.loads(resp.text)
lst = []

for string in dic['array']:
    if not string[:len(dic['prefix'])] == dic['prefix']:
        lst.append(string)
print({'token': verify['token'], 'array': lst})
print('Result: ' + requests.post('http://challenge.code2040.org/api/prefix/validate', data={'token': verify['token'], 'array': lst}).text)
