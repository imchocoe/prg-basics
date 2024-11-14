arr=[2,3,2,5,8,1,9,8]
i=0

arr1=[]
while i<len(arr):
    j=i+1
    sum=0
    while j<len(arr)-1:
        if arr[i]==arr[j] or arr[i]=='a':
            sum+=1
            if arr[i]!='a':
                arr[j]='a'
            break
        j+=1
    
    if sum==0 :
        arr1.append(arr[i])
    i+=1
arr1.remove(arr1[len(arr1)-1])
arr1.remove(arr1[len(arr1)-1])

    
print(arr1)
    
    
    

