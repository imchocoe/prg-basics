arr=[2,6,4,9,7]

def star(n):
    i=0
    stars=[]
    while i<n:
        stars.append("*")
        i+=1
    return stars

i=0
while i<len(arr):
    print(arr[i],':',star(int(arr[i])))
    i+=1