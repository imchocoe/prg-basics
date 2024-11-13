arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
i=0
wynik=' '
while i<len(arr)-1:
    if len(arr[i])>len(arr[i+1]) and len(arr[i])>len(wynik):
        wynik=arr[i]
    i+=1

print(wynik)
