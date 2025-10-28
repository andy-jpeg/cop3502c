from pakudex import *

print("Welcome to Pakudex: Tracker Extraordinaire!")
max_capacity = input("Enter max capacity of the Pakudex: ")

while not max_capacity.isdigit():
    print("Please enter a valid size.")
    max_capacity = input("Enter max capacity of the Pakudex: ")

new_pakudex = Pakudex(max_capacity)
print(f"The Pakudex can hold {max_capacity} species of Pakuri.")

while True:
    print("\nPakudex Main Menu\n-----------------\n1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri\n4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit")

    menu_option = input("\nWhat would you like to do? ")

    if not menu_option.isdigit():
        print("Unrecognized menu selection!")
        continue

    menu_option = int(menu_option)

    if menu_option == 1:
        species_list = new_pakudex.get_species_array()

        if species_list:
            print("Pakuri In Pakudex:")

            for index, species in enumerate(species_list):
                print(f"{index + 1}. {species}")
        else:
            print("No Pakuri in Pakudex yet!")
    elif menu_option == 2:
        species = input("Enter the name of the species to display: ")
        species_name = species
        species = new_pakudex.get_stats(species)
        
        if species:
            print(f"\nSpecies: {species_name}\nAttack: {species[0]}\nDefense: {species[1]}\nSpeed: {species[2]}")
        else:
            print("Error: No such Pakuri!")
    elif menu_option == 3:
        if new_pakudex.get_capacity() == new_pakudex.get_size():
            print("Error: Pakudex is full!")
            continue

        species = new_pakudex.add_pakuri(input("Enter the name of the species to add: "))
        
        if species:
            print(f"Pakuri species {species} successfully added!")
        else:
            print("Error: Pakudex already contains this species!")
    elif menu_option == 4:
        species = new_pakudex.evolve_species(input("Enter the name of the species to evolve: "))

        if species:
            print(species)
        else:
            print("Error: No such Pakuri!")
    elif menu_option == 5:
        new_pakudex.sort_pakuri()
        print("Pakuri have been sorted!")
    elif menu_option == 6:
        print("Thanks for using Pakudex! Bye!")
        break
    else:
        print("Unrecognized menu selection!")