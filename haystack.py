import requests
import json

verify = {'token': 'f1f678e201bd75e55acaa749f3173a25'}
resp = requests.post('http://challenge.code2040.org/api/haystack', data=verify)
print('Received: '+ resp.text)
dic = json.loads(resp.text)
needle_pos = dic['haystack'].index(dic['needle'])
print('Result: ' + requests.post('http://challenge.code2040.org/api/haystack/validate', data={'token': verify['token'], 'needle': needle_pos}).text)
