# 059 - LCM
a = abs(int(input("Enter first integer: ")))
b = abs(int(input("Enter second integer: ")))
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x
if a == 0 or b == 0:
    lcm = 0
else:
    lcm = a * b // gcd
print("LCM:", lcm)
