score=input('Enter score between 0.0 and 1.0: ')
sc=float(score)
grade=sc
if sc>1.0:
    print('Try again frienderino, score must be between 0.0 and 1.0')
    quit()
else: 
    if sc>=0.9:
        print('A')
    elif sc>=0.8:
        print('B')
    elif sc>=0.7:
        print('C')
    elif sc>=0.6:
        print('D')
    elif sc<0.6:
        print('F')