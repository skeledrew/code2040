'''
Comments:
- dateutil.parser module was broken on my system, making it difficult to parse datetime structures.
-- It was quicker and easier to implement my own solution, though it's less efficient.
'''

import requests
import json

verify = {'token': 'f1f678e201bd75e55acaa749f3173a25'}
resp = requests.post('http://challenge.code2040.org/api/dating', data=json.dumps(verify), headers={'content-type': 'application/json'})
print('Received: '+ str(resp.text))
dic = json.loads(resp.text)
secs = int(dic['interval'])

ds = dic['datestamp']
ds_test = "2016-11-28T04:33:23Z" # test
ds_blnk = "0000-00-00T00:00:00Z" # for formatting seconds

def inc_ds(ds, secs):
    lst = []
    # could have done a more efficient split by non-numbers
    lst.append(int(ds[:4])) # year
    lst.append(int(ds[5:7])) # month
    lst.append(int(ds[8:10])) # day
    lst.append(int(ds[11:13])) # hour
    lst.append(int(ds[14:16])) # minute
    lst.append(int(ds[17:19])) # seconds
    mnths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while secs > 0:
        # could have used recursion instead
        lst[5] += 1
        secs -= 1

        if lst[5] > 59:
            lst[5] = 0
            lst[4] += 1

        if lst[4] > 59:
            lst[4] = 0
            lst[3] += 1

        if lst[3] > 23:
            lst[3] = 0
            lst[2] += 1

        if lst[2] > mnths[lst[1]-1]:
            lst[2] = 1
            lst[1] += 1

        if lst[1] > 12:
            lst[1] = 1
            lst[0] += 1
    # could have used a loop and separator list/string to reconstruct this
    ds = str(lst[0])
    ds += '-' + (str(lst[1]) if lst[1] >= 10 else '0' + str(lst[1])) # '+' binding stronger than 'if'
    ds += '-' + (str(lst[2]) if lst[2] >= 10 else '0' + str(lst[2]))
    ds += 'T' + (str(lst[3]) if lst[3] >= 10 else '0' + str(lst[3]))
    ds += ':' + (str(lst[4]) if lst[4] >= 10 else '0' + str(lst[4]))
    ds += ':' + (str(lst[5]) if lst[5] >= 10 else '0' + str(lst[5]))
    ds += 'Z'
    return ds

#for secs in [61, 3600, 3601, 3599, 86400, 86402, 86399, 86403*2+61]:
#    print(ds_test, secs, inc_ds(ds_test, secs))
#    print(ds_blnk, secs, inc_ds(ds_blnk, secs))
ds = inc_ds(ds, secs)
print('To send:', {'token': verify['token'], 'datestamp': ds})
print('Broken-down seconds: 000' + inc_ds(ds_blnk, secs))
print('Result: ' + requests.post('http://challenge.code2040.org/api/dating/validate', data=json.dumps({'token': verify['token'], 'datestamp': ds}), headers={'content-type': 'application/json'}).text)
