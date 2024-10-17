nr_of_hours=int(input('Enter the number of hours:'))
if nr_of_hours >=1 and nr_of_hours<=2:
    print('Amount to pay is 5 PLN')
elif nr_of_hours>=3 and nr_of_hours <=6:
    print('Amount to pay is 15 PLN')
elif nr_of_hours>6:
    print('Amount to pay is 20 PLN')