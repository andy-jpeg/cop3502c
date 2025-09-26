factors = []

def fibonacci(num):
    sum = 0
    value1 = 0
    value2 = 1
    v = 1

    if num == 1:
        return 0
    elif num == 2:
        return 1

    for i in range(0, num - 2):
        sum = value1 + value2
        value1 = value2
        value2 = sum

    return sum

def is_prime(num):
    counter = 0
    num = abs(num)

    for i in range(1, num + 1):
        if num % i == 0 and i != 1 and i != num:
            counter += 1

    if counter == 0:
        return True
    else:
        return False

def find_smaller_factors():
    for v in factors:
        if not is_prime(v):
            factors.remove(v)

            if v % 2 == 0:
                factors.append(v // 2)
                factors.append(v // (v // 2))
            elif v % 3 == 0:
                factors.append(v // 3)
                factors.append(v // (v // 3))
            elif v % 5 == 0:
                factors.append(v // 5)
                factors.append(v // (v // 5))

def print_prime_factors(num):
    previous_factor = 0

    if not is_prime(num):
        for i in range(num + 1, 1, -1):
            if i == 1 or i == num:
                continue

            if num % i == 0:
                if len(factors) == 0:
                    previous_factor = i
                    factors.append(i)

                if i * previous_factor == num:
                    previous_factor = i
                    factors.append(i)

        find_smaller_factors()
        factorable = True

        while factorable:
            for factor in range(len(factors)):
                if factor >= (len(factors) - 1) and is_prime(factors[factor]):
                    factorable = False
                    break
                if not is_prime(factor):
                    find_smaller_factors()
    else:
        factors.append(num)

    factors_list = f"{num} = "
    factors.sort()

    for factor in range(len(factors)):
        if factor >= (len(factors) - 1):
            factors_list += f"{factors[factor]}"
        else:
            factors_list += f"{factors[factor]} * "

    print(factors_list)

print_prime_factors(1000)