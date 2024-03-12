maximum=None
minimum=None
while True:
    numberino=input('Enter numberino: ')
    if numberino=='done':
        break
    try:
        numberino=int(numberino)
    except:
        print('Invalid input')
        continue
    for largest in [numberino]:
        if maximum is None:
            maximum=numberino
        elif largest>maximum:
            maximum=largest
    for smallest in [numberino]:
        if minimum is None:
            minimum=smallest
        elif smallest<minimum:
            minimum=smallest
print('Maximum is',maximum)
print('Minimum is',minimum)