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

def display_menu():
    print("\nRLE Menu\n--------")
    print("0. Exit\n1. Load File\n2. Load Test Image\n3. Read RLE String\n4. Read RLE Hex String\n5. Read Data Hex String\n6. Display Image\n7. Display RLE String\n8. Display Hex RLE Data\n9. Display Hex Flat Data")

def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")

    console_gfx.display_image(console_gfx.test_rainbow)

    while True:
        display_menu()
        menu_option = int(input("Select a Menu Option: "))

        if menu_option == 0:
            break
        elif menu_option == 1:
            file_name = input("Enter the name of the file: ")
            image_data = console_gfx.load_file(file_name)
        elif menu_option == 2:
            image_data = console_gfx.test_image
            print("Test image data is loaded")
        elif menu_option == 3:
            pass
        elif menu_option == 4:
            pass
        elif menu_option == 5:
            pass
        elif menu_option == 6:
            console_gfx.display_image(image_data)
        elif menu_option == 7:
            pass
        elif menu_option == 8:
            pass
        elif menu_option == 9:
            pass

# if __name__ == "__main__":
#     main()