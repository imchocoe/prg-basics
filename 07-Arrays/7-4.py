###
# Prints some array elements
#the array
#number of elements
#first value
#second value
#last value
#last but one value (do not use negative index values)
#sum of the first and last value
#middle value
#all array values separated by a single space (use a loop statement)
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print("Last Value",arr[-1])
print('Last but one value', len(arr)-1)
print('Sum of the firdt and last value',arr[0]+arr[-1])
print('Middle value', arr[len(arr)//2])
i=0
while i<len(arr):
    print(arr[i],end=" ")
    i+=1