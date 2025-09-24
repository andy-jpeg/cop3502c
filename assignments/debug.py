size = int(input("Enter an odd number from 3 to 9: "))
height = size // 2 + 1

for i in range(1, height + 1):
    print(" " * (height - i), end="")
    for j in range(1, i * 2):
        print(j, end="")