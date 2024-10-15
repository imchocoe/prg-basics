###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0
nr=0
# Calculate the sum of even numbers
while nr<N:
    if nr % 2 == 0:
        sum_even += nr
    nr+=1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")