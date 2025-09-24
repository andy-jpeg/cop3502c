legs = input("Does it have legs [y/n]: ")

if legs == "y":
    fluffy = input("Is it fluffy [y/n]: ")
    if fluffy == "y":
        print("It's a cat!")
    else:
        print("It's a gator!")
elif legs == "n":
    land = input("Does it live on land [y/n]: ")
    if land == "y":
        print("It's a snake!")
    else:
        print("It's a shark!")