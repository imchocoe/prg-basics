text=input('Enter text :')
letter=input('Enter letter:')
def how_many(letter):

    i=0
    count=0
    while i<len(text):
        if text[i]==letter:
            count+=1
        i+=1

    return count


print(f'The number of letter "{letter}": {how_many(letter)}')

