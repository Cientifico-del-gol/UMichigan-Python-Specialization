import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url=input('Enter URL: ')
co=int(input('Enter count: '))
po=int(input('Enter position: '))

for i in range(co):
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    countc=0
    for tag in tags:
        countc+=1
        if countc>po:
            break
        url=tag.get('href', None)
    print('Retrieving:',url)