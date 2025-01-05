from functools import reduce
def add(x,y):
    return x+y
numbers = [2,4,6,3,7,5]
wyn=reduce(add,filter(lambda a:a%2 ==0,numbers))
print(wyn)