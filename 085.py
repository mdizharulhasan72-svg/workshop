# 085 - Hollow rectangle
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
for i in range(rows):
    if i == 0 or i == rows - 1:
        print("* " * cols)
    else:
        print("* " + "  " * max(0, cols - 2) + ("*" if cols > 1 else ""))
