###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#72, 65, 64, 18, 17
age = int(input('Enter your age: '))

if age < 18 or age>=65 :
    print('Discount available')
else:
    print('No discount for you :(')