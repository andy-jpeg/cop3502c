def flatten(nested_list):
    new_List = []

    for i in nested_list:
        if type(i) == list:
            new_List += flatten(i)
        else:
            new_List.append(i)

    return new_List

def mystery1(n):
    a, b, c, d, e = 1, 2, 3, 4, 5

    for _ in range(n):
        temp = a - c + e
        a = b
        b = c
        c = d
        d = e

        e = temp

    return a

def mystery2(number):
    total = 0

    if number > 0:
        total += (number % 10) + mystery2(number // 10)

    return total

def collatz_sequence(n):
    print(n, end=" ")

    if n == 1:
        print()
    elif n % 2 == 0:
        collatz_sequence(int(n / 2))
    else:
        collatz_sequence(int(3 * n + 1))