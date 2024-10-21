for i in range(1,31):
    if i%3==0 and i%5==0:
        print('Bingo')
    elif i%3==0:
        print('three')
    elif i%5==0:
        print('five')
    else:
        print(i)
    