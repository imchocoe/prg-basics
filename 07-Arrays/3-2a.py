arr=[15, 8, 31, 47, 2, 19]
i=0
arr1=[]
while i<len(arr):
    arr1.append(arr[-(i+1)])
    i+=1

print(arr)
print(arr1)