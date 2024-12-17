sentence = input()

result = list(map(lambda word:len(word), sentence.split()))
print(result)