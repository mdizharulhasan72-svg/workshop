# 088 - Number triangle (row number repeated)
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" ".join([str(i)] * i))
