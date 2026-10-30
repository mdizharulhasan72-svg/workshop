# 056 - Prime number check
n = int(input("Enter an integer: "))
is_prime = n >= 2
i = 2
while i * i <= n and is_prime:
    if n % i == 0:
        is_prime = False
    i += 1
print("Prime" if is_prime else "Not prime")
