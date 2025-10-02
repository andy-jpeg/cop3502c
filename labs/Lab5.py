hex_dictionary = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}

def hex_char_decode(digit):
    if type(digit) == str:
        for index, num in hex_dictionary.items():
            if digit == index:
                return num

        return digit
    else:
        for index, num in hex_dictionary.items():
            if digit == num:
                return index.upper()
            
        return digit

def hex_string_decode(hex):
    previousBit = ""

    for bit in hex: # check for 0b
        if bit == "x" and previousBit == "0":
            hex = hex[2:len(hex)]
        else:
            previousBit = bit

    hex = hex.lower()

    result = 0
    index = 0

    for i in reversed(hex):
        result += int(hex_char_decode(i)) * (16 ** index)
        print(result)

        index += 1
    
    return result

def binary_string_decode(binary):
    previousBit = ""

    for bit in binary: # check for 0b
        if bit == "b" and previousBit == "0":
            binary = "00" + binary[2:len(binary)]
        else:
            previousBit = bit
    
    index = 0
    result = 0

    for power in reversed(binary):
        result += (int(power) * (2 ** index))
        index += 1

    return result

def binary_to_hex(binary):
    previousBit = ""

    for bit in binary: # check for 0b
        if bit == "b" and previousBit == "0":
            binary = "00" + binary[2:len(binary)]
        else:
            previousBit = bit

    binary = binary.lower()

    constructors = []
    constructor = ""

    if len(binary) % 4 != 0:
        binary += ("0" * (len(binary) % 4))

    for bit in binary:
        constructor += bit

        if len(constructor) == 4:
            constructors.append(constructor)
            constructor = ""

    result = ""

    for i in constructors:
        index = 0
        sum = 0

        for j in reversed(i):
            if j == int(j):
                sum += hex_char_decode(j) * (2 ** index)
            else:
                sum += int(j) * (2 ** index)

            print(j)
            index += 1

        if sum >= 10:
            result += hex_char_decode(sum)
        else:
            result += str(sum)
    
    return result

while True:
    print("Decoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit\n")
    menu_option = int(input("Please enter an option: "))

    if menu_option != 4:
        string = input("Please enter the numeric string to convert: ")
        result = 0

        if menu_option == 1: # hexadecimal to decimal
            result = hex_string_decode(string)
        elif menu_option == 2: # binary to decimal
            result = binary_string_decode(string)
        elif menu_option == 3: # binary to hexadecimal
            result = binary_to_hex(string)

        print(f"Result: {result}\n")
    elif menu_option == 4:
        print("Goodbye!")
        break