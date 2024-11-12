categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

a=max(expenses)

i=0
x=""
while i<len(categories):
    if a==expenses[i]:
        x=categories[i]
    i+=1

print(x)
