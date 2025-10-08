import console_gfx as console_gfx

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
        elif menu_option == 6:
            console_gfx.display_image(image_data)

if __name__ == "__main__":
    main()