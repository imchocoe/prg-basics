def f(number,even):
    i=0
    sum=0
    num=str(number)
    if even==True:
        while i< len(num):
            if int(num[i])%2==0:
                nr=int(num[i])
                sum+=nr
            i+=1
    if even==False:
        while i< len(num):
            if int(num[i])%2!=0:
                nr=int(num[i])
                sum+=nr
            i+=1
    return sum

        
sample=f(3124,True)
print(sample)