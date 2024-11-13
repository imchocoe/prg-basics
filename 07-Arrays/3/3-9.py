arr1=["water","book","sky"]
arr2=[1,2,3]
def f(arr1,arr2):
    wynik=False
    if len(arr1)==len(arr2):
        i=0
        sum=0
        while i<len(arr1):
            if arr1[i]==arr2[i]:
                sum+=1
            i+=1
        if sum==len(arr1):
            wynik=True

    return wynik

com=''
if f(arr1,arr2)==True:
    com='they are the same'
else:
    com='not the same'

print(arr1)
print(arr2)
print(com)
            

