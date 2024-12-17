#Define an anonymous function is_even(number) that checks whether a number is even. Then test it by writing a program.
number=int(input('Enter number: '))
is_even=lambda number: number%2
result=is_even(number)
if result==0:
    print(f'The number {number} is even')
else:
    print(f'The number {number} is odd')