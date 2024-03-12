import urllib.request, urllib.parse, urllib.error
import json

url=input('Enter linkerino: ')
uh=urllib.request.urlopen(url)

jsparse=json.loads(uh.read())  
com=jsparse['comments']

total=0
for item in com:
    num=item['count']
    total+=num
print('Sum:',total)