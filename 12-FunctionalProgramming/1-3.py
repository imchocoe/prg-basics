#Write a program that converts speed in meters per second to speed in kilometers per hour. Define a function ms_to_kmh(ms) that returns the calculated speed in km/h. Sample result:

#10 m/s = 36 km/h
#35 m/s = 126 km/h

conv= lambda x: x*3.6

x=int(input())
result=conv(x)
print(x,result)