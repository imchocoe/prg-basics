amount=int(input('Enter the amount in PLN:'))
five=amount//5
two=(amount%5)//2
one=(amount%5)%2

print(f'The amount of PLN {amount}:')
print(f'5 PLN coins: {five}')
print(f'2 PLN coins: {two}')
print(f'1 PLN coins: {one}')

