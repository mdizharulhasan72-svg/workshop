# 068 - Largest and smallest digit
n = abs(int(input("Enter an integer: ")))
digits = [int(digit) for digit in str(n)]
print("Largest digit:", max(digits))
print("Smallest digit:", min(digits))
