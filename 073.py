# 073 - Read numbers until -1, then count and average
count = 0
total = 0.0
while True:
    number = float(input("Enter a number (-1 to stop): "))
    if number == -1:
        break
    total += number
    count += 1
if count:
    print("Count:", count)
    print("Average:", total / count)
else:
    print("No numbers were entered")
