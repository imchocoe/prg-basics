a=tuple('1020304050')
#0-8,2-6,4-4,6-2,8-0
i=0
j=8
arr=[]
while i<len(a):
    arr.append(a[j])
    i+=1
    j-=1
print(arr)

