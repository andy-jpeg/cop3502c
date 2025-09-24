def sum(*args):
    num = 0.0

    for i in args:
        num += i

    return num

def print_range(lower, upper):
    for num in range(lower, upper + 1):
        if num == upper:
            print(upper)
        else:
            print(f"{num},", end=" ")

def sum_of_digits(number):
    digits = 0

    for digit in str(number):
        digits += int(digit)

    return digits