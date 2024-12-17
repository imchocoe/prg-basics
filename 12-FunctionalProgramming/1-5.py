#Write a program that calculates the average speed of a vehicle. Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. Define a function avg_speed(distance,hours,minutes) that returns the calculated average speed. Sample result:

#Enter distance in km: 70
#Enter number of travel hours: 1
#Enter number of travel minutes: 23
#Average speed: 50.6 km/h 

x=int(input('Enter distance in km: '))
y=int(input('Enter a number of travel hours:'))
z=int(input('Enter a number of travel  minutes: '))


avg=lambda x,y,z: round(x/(y+z/60),2)

result=avg(x,y,z)

print(f'Average speed: {result} km/h')