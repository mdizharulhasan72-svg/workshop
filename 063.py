# 063 - Calculate x^n without pow()
x = float(input("Enter x: "))
n = int(input("Enter integer exponent n: "))
if x == 0 and n < 0:
    print("Undefined: zero cannot have a negative exponent")
else:
    result = 1
    for _ in range(abs(n)):
        result *= x
    if n < 0:
        result = 1 / result
    print("Result:", result)
