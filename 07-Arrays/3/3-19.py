a=int(input())
arr=[1,2,3,4,5,6,7,8,9,10]
wynik=[]
i=0
while i< len(arr):
    if arr[i]>a:
        wynik.append(arr[i])
    i+=1
print(wynik)