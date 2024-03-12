import re
file=open('sample data.txt')
fr=file.read()
integers=re.findall('[0-9]+',fr)
count=0
for num in integers:
    num=int(num)
    count=count+num
print(count)