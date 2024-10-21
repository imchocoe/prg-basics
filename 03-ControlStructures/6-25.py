
attempt=0
while attempt<3:
    pin=input('Enter PIN code:')
    if pin=="0805":
        print('Payment accepted')
    else:
        print('Incorrect')
    attempt+=1
if attempt==3 and pin !="0805":
    print('Sorry the card has been blocked')