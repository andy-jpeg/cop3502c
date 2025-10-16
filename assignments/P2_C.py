import console_gfx as console_gfx

hex_table = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

def to_hex_string(data):
    hex_string = ""

    for num in data:
        if num >= 10:
            hex_string += hex_table[num]
        else:
            hex_string += str(num)

    return hex_string

def count_runs(flat_data):
    count = 0
    num_counter = 1
    previous_num = -1

    for num in flat_data:
        if previous_num == num:
            num_counter += 1

            if num_counter >= 15:
                num_counter = 1
                previous_num = -1

                continue
        else:
            count += 1
            num_counter = 1
        
        previous_num = num

    return count

def encode_rle(flat_data):
    rle = []
    count = 1
    previous_num = -1

    for num in flat_data:
        if previous_num == num:
            count += 1

            if count >= 15:
                count = 1
                previous_num = -1

                rle[len(rle) - 2] = 15

                continue
            else:
                rle[len(rle) - 2] = count
        else:
            count = 1

            rle.append(count)
            rle.append(num)
        
        previous_num = num

    return rle

def get_decoded_length(rle_data):
    count = 0
    counter = 0

    for i in rle_data:
        if counter % 2 == 0:
            count += i

        counter += 1
    
    return count

def decode_rle(rle_data):
    flat_data = []
    multiplier = 0
    counter = 0

    for num in rle_data:
        if counter % 2 == 0:
            multiplier = num
            for i in range(multiplier):
                flat_data.append(rle_data[counter + 1])

        counter += 1

    return flat_data

def string_to_data(data_string):
    rle_data = []

    for num in data_string:
        if num.isdigit():
            rle_data.append(int(num))
        else:
            for i, v in hex_table.items():
                if v == num:
                    rle_data.append(i)

    return rle_data

def to_rle_string(rle_data):
    rle_string = ""

    for i, num in enumerate(rle_data):
        if i % 2 == 0 and i != 0:
            rle_string += ":" + str(num)
        else:
            if num >= 10:
                rle_string += hex_table[num]
            else:
                rle_string += str(num)

    return rle_string

def string_to_rle(rle_string):
    rle_data = []
    delimiter = False

    rle_string = rle_string.split(":")

    for byte in rle_string:
        hex = False

        for i, v in hex_table.items():
            if v == byte[-1]:
                hex = not hex

                rle_data.append(int(byte[0:-1]))
                rle_data.append(int(i))

        if not hex:
            for i, num in enumerate(byte):
                if hex_table.get(int(byte[0:-1])) and len(byte) == 3:
                    rle_data.append(hex_table[int(byte[0:-1])])
                    rle_data.append(int(byte[-1]))
                    break
                else:
                    rle_data.append(int(num))

    return rle_data

def hex_to_flat(hex_list):
    hex_string = ""

    for char in hex_list:
        hex_string += str(char)

    return hex_string

def display_menu():
    print("\nRLE Menu\n--------")
    print("0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data")

def main():
    rle = []
    rle_string = ""
    rle_hex_string = ""

    flat_string = ""
    flat_hex = ""

    image_data = None

    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")

    console_gfx.display_image(console_gfx.test_rainbow)

    while True:
        display_menu()
        menu_option = int(input("\nSelect a Menu Option: "))

        if menu_option == 0:
            break
        elif menu_option == 1:
            file_name = input("Enter the name of the file: ")
            image_data = console_gfx.load_file(file_name)

            flat_string = image_data

            rle = encode_rle(flat_string)
            rle_string = to_rle_string(rle)
            rle_hex_string = to_hex_string(string_to_rle(rle_string))
        elif menu_option == 2:
            image_data = console_gfx.test_image
            flat_string = image_data

            rle = encode_rle(flat_string)
            rle_string = to_rle_string(rle)
            rle_hex_string = to_hex_string(string_to_rle(rle_string))

            flat_hex = to_hex_string(flat_string)

            print("Test image data loaded.")
        elif menu_option == 3:
            rle_string = input("Enter an RLE string to be decoded: ").lower()
            rle_hex_string = string_to_rle(rle_string)
            rle_hex_string = hex_to_flat(rle_hex_string)

            flat_hex = hex_to_flat(decode_rle(string_to_data(rle_hex_string)))
            image_data = string_to_rle(rle_string)
        elif menu_option == 4:
            rle_hex_string = input("Enter the hex string holding RLE data: ").lower()
            rle_string = to_rle_string(string_to_data(rle_hex_string))

            flat_hex = hex_to_flat(decode_rle(string_to_data(rle_hex_string)))
            image_data = rle_string
        elif menu_option == 5:
            flat_hex = input("Enter the hex string holding flat data: ")
            rle = encode_rle(string_to_data(flat_hex))

            rle_string = to_rle_string(rle)
            rle_hex_string = to_hex_string(rle)

            image_data = string_to_rle(rle_string)
        elif menu_option == 6:
            print("Displaying image...")
            console_gfx.display_image(image_data) if image_data else print("(no data)")
        elif menu_option == 7:
            print("RLE representation: ", end="")
            print(rle_string) if image_data else print("(no data)")
        elif menu_option == 8:
            print("RLE hex values: ", end="")
            print(rle_hex_string) if image_data else print("(no data)")
        elif menu_option == 9:
            print("Flat hex values: ", end="")
            print(flat_hex) if image_data else print("(no data)")
        else:
            print("Error! Invalid input.")
            continue

if __name__ == "__main__":
    main()