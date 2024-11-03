def f(name):
    words=name.split()
    wynik=''.join(word[0] for word in words)
    return wynik

if __name__=="__main__":
    print(f('For Your Information'))