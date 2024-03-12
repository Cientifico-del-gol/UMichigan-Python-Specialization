import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url=input('Enter location: ')
uh=urllib.request.urlopen(url)

tree=ET.fromstring(uh.read())
lst=tree.findall('.//count')    

total=0

for numb in lst:
    numberino=int(numb.text)
    total+=numberino
print('Sum:',total)