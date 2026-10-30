# 034 - Roots of a quadratic equation
import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
if a == 0:
    print("Not a quadratic equation (a must not be zero)")
else:
    d = b * b - 4 * a * c
    if d > 0:
        print("Two real roots:", (-b + math.sqrt(d)) / (2 * a), "and", (-b - math.sqrt(d)) / (2 * a))
    elif d == 0:
        print("Equal real roots:", -b / (2 * a))
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-d) / abs(2 * a)
        print(f"Imaginary roots: {real}+{imag}i and {real}-{imag}i")
