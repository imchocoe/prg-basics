arr=[[1,2,3,4,5],
     [6,7,8,9,1],
     [2,3,4,5,6]]
i=0
arr1=[]
arr2=[]
while i<5:
    arr1.append(arr[0][i])
    arr2.append(arr[2][i])
    i+=1
arr[0].clear()
arr[2].clear()

arr[0].append(arr1)
arr[2].append(arr1)

print(arr[0])
print(arr[1])
print(arr[2])