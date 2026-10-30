# 054 - Print digits from left to right
n = input("Enter an integer: ").strip()
digits = n.lstrip("-")
if digits.isdigit() and digits:
    for digit in digits:
        print(digit)
else:
    print("Invalid integer")
