#Number ... is positive
#Number ... is negative
#Number is 0

number=int(input("Enter number:"))
if number>0:
    print(f'Number {number} is positive')
elif number<0:
    print(f'Number {number} is negative')
elif number==0:
    print(f"Number is 0")