import requests

verify = {'token': 'f1f678e201bd75e55acaa749f3173a25'}
resp = requests.post('http://challenge.code2040.org/api/reverse', data=verify)
print('Received: '+ resp.text)
rev_str = resp.text[::-1]
print('Result: ' + requests.post('http://challenge.code2040.org/api/reverse/validate', data={'token': verify['token'], 'string': rev_str}).text)
