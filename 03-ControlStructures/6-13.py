fb=input('Do you use facebook? (Y/N):')
x=input('Do you use twitter? (Y/N):')
ig=input('Do you use instagram? (Y/N):')
socialmedias=0

if fb=="Y":
    socialmedias+=1
if x=="Y":
    socialmedias+=1
if ig=="Y":
    socialmedias+=1

if socialmedias>=2:
    print('You are a good influencer :)')
else:
    print('Maybe you should use more apps?')