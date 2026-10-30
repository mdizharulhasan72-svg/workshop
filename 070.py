# 070 - Perfect number
n = int(input("Enter a positive integer: "))
if n <= 1:
    print("Not a perfect number")
else:
    total = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    print("Perfect number" if total == n else "Not a perfect number")
