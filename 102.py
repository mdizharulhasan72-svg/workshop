# 102 - Alphabet pyramid: A B C ... then reverse
n = int(input("Enter number of rows (1-26): "))
for i in range(1, min(n, 26) + 1):
    print("  " * (n - i), end="")
    letters = [chr(64 + j) for j in range(1, i + 1)]
    print(" ".join(letters + letters[-2::-1]))
