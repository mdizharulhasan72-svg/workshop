# 076 - Count vowels in a string using recursion
def count_vowels(text):
    if not text:
        return 0
    current = 1 if text[0].lower() in "aeiou" else 0
    return current + count_vowels(text[1:])

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))
