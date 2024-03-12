file=input("Enter file: ")
fh=open(file)
t_h=dict()
for line in fh:
    if line.startswith('From '):
        cont=line.split()
        fullhour=cont[5]
        hoursent=fullhour.split(':')
        hour=hoursent[0]
        t_h[hour]=t_h.get(hour,0)+1
neot_h=sorted(t_h.items())
for k,v in neot_h:
    print(k,v)