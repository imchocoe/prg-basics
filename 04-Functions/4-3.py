import math
def triangle_area(a,b,c):
    s=(a+b+c)/2
    A=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return A

area=triangle_area(7,24,25)
print(area)