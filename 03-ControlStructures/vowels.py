###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
x=0
# Count vowels in the text
#for char in text:
   # if char in vowels:
      #  vowel_count += 1

#print(f"The number of vowels in the text is: {vowel_count}")


while x<len(text):
    if text[x] in vowels:
        vowel_count+=1
    x+=1
print(vowel_count)