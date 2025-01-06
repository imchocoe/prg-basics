d={"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
wyn=list(filter(lambda x:d[x]>0,d))
print(wyn)