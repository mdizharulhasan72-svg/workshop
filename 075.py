# 075 - String palindrome using recursion
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

s = input("Enter a string: ").lower().replace(" ", "")
print("Palindrome" if is_palindrome(s) else "Not a palindrome")
