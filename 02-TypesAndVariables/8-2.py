###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# c to k 
# c to f


c=float(input('temperature in celsius:',))
k=c+273.15
f=(c*9/5)+32
print(f'temperature in kelvins:{k} and in fahrenheits: {f}')