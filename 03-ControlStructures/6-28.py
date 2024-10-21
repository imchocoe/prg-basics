nr=int(input('Enter number range:'))
i=2
deadline=0
x=2
for i in range (nr):
    for x in range (i):
        if i%x==0:
            deadline+=1
        x+=1
    if deadline>0:
        print(i)  
    i+=1    
