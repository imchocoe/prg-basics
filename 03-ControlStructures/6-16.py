time=(input('Enter time (24-hour format):'))
if int(time[0:2])>12:
    hours=int(time[0:2])
    calc=hours-12
    print(f'Time in 12-hour format:{calc}:{time[3:5]}pm')
else:
    print(f'Time in 12-hour format:{time}am')