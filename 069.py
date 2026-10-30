# 069 - Factors / divisors
n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer")
else:
    print("Factors:", end=" ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()
