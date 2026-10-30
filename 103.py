# 103 - Butterfly pattern
n = int(input("Enter half-height: "))
for i in range(1, n + 1):
    left = "* " * i
    gap = "  " * (2 * (n - i))
    print(left + gap + left)
for i in range(n, 0, -1):
    left = "* " * i
    gap = "  " * (2 * (n - i))
    print(left + gap + left)
