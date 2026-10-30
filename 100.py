# 100 - Reverse alphabet triangle
n = int(input("Enter number of rows (1-26): "))
for i in range(min(n, 26), 0, -1):
    print(" ".join(chr(64 + j) for j in range(1, i + 1)))
