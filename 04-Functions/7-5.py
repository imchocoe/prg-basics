x=int(input('Enter x:'))
y=int(input("Enter y:"))
num=int(input('Enter number:'))
def number(x,y):
    isit=False
    if num >=x and num<=y:
        isit=True
    return isit

print(f'Number {num} in the range <{x},{y}>: {number(x,y)}')
    