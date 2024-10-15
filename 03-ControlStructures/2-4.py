###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input('Enter number:'))
number2 = int(input('Enter another number:'))
operator = input('Enter a symbol of mathematical operation:')
if operator== "+":
    answer=number1+number2
elif operator=="-":
    answer=number1-number2
elif operator=="*":
    answer=number1*number2
elif operator=="/":
    answer=number1/number2
else:
    print('wrong operator')
print(f'Your answer is {answer}')