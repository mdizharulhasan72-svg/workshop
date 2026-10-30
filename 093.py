# 093 - Number pyramid centered (ascending then descending sequence shown by example)
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print(" ".join(str(j) for j in range(1, 2 * i)))
