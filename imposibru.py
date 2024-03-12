name=input("Enter file:")
fh=open(name)
mailtots=dict()
for line in fh:
    if line.startswith('From '):
        cont=line.split()
        mail=cont[1]
        mailtots[mail]=mailtots.get(mail,0)+1
biguscount=None
bigusmail=None
for mail,count in mailtots.items():
    if biguscount is None or count>biguscount:
        biguscount=count
        bigusmail=mail
print(bigusmail,biguscount)
