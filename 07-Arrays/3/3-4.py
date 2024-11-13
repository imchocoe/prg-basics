arr=[-15, 8, -31, 47, -2, 19]
#max
i=0
max=0
while i<len(arr)-1:
    if arr[i]>arr[i+1] and arr[i]>max:
        max=arr[i]
    i+=1
#min
j=0
min=0
while j<len(arr)-1:
    if arr[j]<arr[j+1] and arr[j]<min:
        min=arr[j]
    j+=1


print(max,min)
