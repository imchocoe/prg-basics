def ndlarge(array):
    i=0
    wynik=0
    while i<len(array)-1:
        if array[i]<array[i+1]:
            wynik =array[i+1]
        i+=1
    a=wynik-1
    if a in array:
        win=a    
    return a

def diff(array):
    a=max(array)
    b=min(array)
    wynik=a-b
    return wynik

def median(array):
    sum=0
    for i in array:
        sum+=i
    wynik=sum/len(array)
    return wynik

def sm(array):
    a=max(array)
    b=min(array)
    return a,b

arr=[7,3,8,5,2]
print(arr)
print(ndlarge(arr))
print(median(arr))
print(sm(arr))

