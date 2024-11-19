with open('pets.txt','r') as file:
    content=file.read()
    lines=content.split()
total=0
for line in lines:
    total+=1
print(total)