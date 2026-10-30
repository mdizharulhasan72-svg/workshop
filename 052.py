# 052 - Happy number
n = int(input("Enter a positive integer: "))
seen = set()
while n != 1 and n not in seen and n > 0:
    seen.add(n)
    total = 0
    for digit in str(n):
        total += int(digit) ** 2
    n = total
print("Happy number" if n == 1 else "Not a happy number")
