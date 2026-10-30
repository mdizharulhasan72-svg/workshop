# 067 - General Armstrong number
n = int(input("Enter a non-negative integer: "))
digits = str(n)
power = len(digits)
total = sum(int(digit) ** power for digit in digits)
print("Armstrong number" if total == n else "Not an Armstrong number")
