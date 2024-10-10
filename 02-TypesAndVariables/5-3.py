###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
astr = input('a=',)
a=int(astr)
bstr = input('b=',)
b=int(bstr)
cstr = input('c=',)
c=int(cstr)

volume=a*b*c
sarea=2*(a*b+a*c+b*c)
print(f'the volume is:{volume}')
print(f'the surface area is:{sarea}')