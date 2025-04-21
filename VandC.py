str = input("Enter a string: ")
vowels = "aeiouAEIOU"
def is_vowel(char):
    return char in vowels
length = len(list(filter(is_vowel,str)))
print(length)
