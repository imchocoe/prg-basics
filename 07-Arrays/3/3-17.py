a=tuple('50,20,40,50,30,50')
def f(number,tuple):
    num=str(number)
    x=(num[0])
    y=(num[1])
    i=0
    j=1
    wynik=0
    while i<len(tuple)-1:  
        if tuple[i]==x and tuple[j]==y:
            wynik+=1
        i+=1
        j+=1
    return wynik

print(f(50,a))
