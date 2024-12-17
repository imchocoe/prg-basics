#Define an anonymous function initials(name,surname) that returns the first letters of the name and surname.

name=input()
surname=input()
initials=lambda name,surname: name[0]+surname[0]

print(initials(name,surname))