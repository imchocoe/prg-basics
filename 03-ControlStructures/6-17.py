x=int(input('X:'))
y=int(input('Y:'))

if x==0 and y==0:
    print('Plane on 00')
elif x==0 and y>0:
    print('Sth between 1 and 2')
elif x==0 and y<0:
    print('Sth between 3 and 4')
elif x>0 and y==0:
    print ('Sth between 1 and 4')
elif x<0 and y==0:
    print('Sth between 2 and 3')
elif x>0 and y>0:
    print('First quadrant')
elif x<0 and y>0:
    print('Second quadrant')
elif x<0 and y<0:
    print('Third quadrant')
elif x>0 and y<0:
    print('Fourth quadrant')
    