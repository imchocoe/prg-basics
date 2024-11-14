def f(number,array):
    wynik=False
    if number in array:
        wynik=True
    return wynik

result=f(23,[15, 38, 7, 23, 14])
print(result)