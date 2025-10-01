def hex_char_decode(digit):
    print()

def hex_string_decode(hex):
    print()

def binary_string_decode(binary):
    print()

def binary_to_hex(binary):
    print()

while True:
    print("Decoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit\n")
    menu_option = int(input("Please enter an option: "))

    if menu_option != 4:
        string = input("Please enter the numeric string to convert: ")
        result = 0

        if menu_option == 1: # hexadecimal to decimal
            
        elif menu_option == 2: # binary to decimal

        elif menu_option == 3: # binary to hexadecimal

    elif menu_option == 4:
        print("Goodbye!")
        break