import math
spacing = " "

def fourbonacci(n):
    a, b, c, d = 1, 4, 7, 8

    for i in range(n - 1):
        sum = (a * 4) + (b * 3) + (c * 2) + d
        a = b
        b = c
        c = d
        d = sum
    
    return a

def odd_squares(n):
    counter = 0
    
    while n > counter:
        for i in range(1, n * 2):
            if i % 2 != 0:
                print(i ** 2)
                counter += 1

def diamond(n):
    for i in range(0, n + 1, 2):
        for k in range(1, n + 1):
            spaces = n - i
            sequence = " "

            sequence += (spacing * (spaces // 2))
            
            for m in range(1, i):
                sequence += str(m)

            sequence += (spacing * (spaces // 2))

            print(sequence)
            break
    
    for i in range(n + 1, 1, -2):
        for k in range(1, n + 1):
            spaces = n - i
            sequence = " "
            if i == n + 1:
                sequence = ""


            sequence += (spacing * (spaces // 2))
            
            for m in range(1, i):
                sequence += str(m)

            sequence += (spacing * (spaces // 2))

            print(sequence)
            break