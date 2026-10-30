# 105 - Number diamond
n = int(input("Enter half-height: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print(" ".join(str(j) for j in list(range(1, i + 1)) + list(range(i - 1, 0, -1))))
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print(" ".join(str(j) for j in list(range(1, i + 1)) + list(range(i - 1, 0, -1))))
