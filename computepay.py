hours=input('Hours worked: ')
h=float(hours)
rate=input('Enter rate: ')
r=float(rate)
def computepay():
    if h<=40:
        return(h*r)
    else:
        return((h*r)+((h-40)*(r*0.5)))
print('Pay',computepay())