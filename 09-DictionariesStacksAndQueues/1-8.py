price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}



for key,values in price_list.items():
    print(key,values)

total=0

for values in price_list.values():
    total +=int(values)
print(total)
sum=0
for key,values in price_list.items():
    i=values*0.9
    price_list[key]=i
    sum+=i
    print(key,round(i,2))
print(round(sum,2))

