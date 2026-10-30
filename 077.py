# 077 - Print increasing then decreasing using one recursive function
def print_up_down(n, current=1):
    if current > n:
        return
    print(current, end=" ")
    print_up_down(n, current + 1)
    print(current, end=" ")

n = int(input("Enter N: "))
if n >= 1:
    print_up_down(n)
print()
