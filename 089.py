# 089 - Sequential number triangle
n = int(input("Enter number of rows: "))
value = 1
for i in range(1, n + 1):
    for j in range(i):
        print(value, end=" ")
        value += 1
    print()
