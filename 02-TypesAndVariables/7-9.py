import random 
dr1=random.randint(1,6)
special=dr1==1 or dr1==6

print(f'dice rolled:{dr1}')
print(f'special number:{special}')