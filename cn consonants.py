text = "python"
vowels = 0
consonants = 0
for char in text.lower():
    if char in "aeiou":
        vowels += 1
    elif char .isalpha():
        consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)


#cn words
text = "python is very easy"
words = text.split()
print("number of words =", len(words))


# reverse wordsd
text = "python is very easy"
words = text.split()
for word in words:
    print(word[::-1], end = " ") 

#remove space

text = "python  programming"
new_text = text.replace(" ", "")
print(new_text)