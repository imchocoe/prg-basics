
def f(binary_number):
    i=0
    nr=0
    yn=False
    while i<len(binary_number):
        if binary_number[i]=="1" or binary_number[i]=="0":
            
            nr+=1
        i+=1
        
    if nr==len(binary_number):
        yn=True
    return yn


one=f('101101')
two= f("1311a10100")

print(one)
print(two)


        
    
        
