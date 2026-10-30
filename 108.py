# 108 - Right arrow pattern
n = int(input("Enter arrow height (at least 3): "))
middle = n // 2
for i in range(n):
    if i < middle:
        print("*")
    elif i == middle:
        print("* " * (middle + 1))
    else:
        print("* " * max(1, n - i))
