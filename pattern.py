height = int(input("Height: "))
num = ""

for i in range(1, height + 1):
    num += str(i)
    spacing = ""
    for j in range(height, i, -1):
        spacing += " "
    print(spacing + str(num))