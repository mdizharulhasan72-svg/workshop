# 104 - Hollow diamond inside rectangle (outline approximation)
n = int(input("Enter half-height: "))
width = 2 * n + 1
for i in range(-n, n + 1):
    edge = abs(i)
    row = []
    for j in range(width):
        if j == 0 or j == width - 1 or abs(j - n) == edge:
            row.append("*")
        else:
            row.append(" ")
    print(" ".join(row))
