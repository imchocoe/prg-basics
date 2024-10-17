name=input('Enter your name:')
name_len=len(name)-1
letter=name[name_len]
if letter== 'a':
    print(f'{name} is a Polish female name.')
else:
    print(f'{name} is not a Polish female name.')