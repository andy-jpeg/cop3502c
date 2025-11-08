import sys
import heifer_generator
from dragon import Dragon

arguments = sys.argv
arguments = arguments[1:]

first_arg = arguments[0]

def find_cows(cow_name):
    for cow in heifer_generator.get_cows():
        if cow.name == cow_name:
            return cow
        
    return None

if first_arg == "-l":
    cow_names = ""

    for cow in heifer_generator.get_cows():
        cow_names += cow.name + " "

    print(f"Cows available: " + cow_names)
elif first_arg == "-n":
    cow_name = arguments[1]
    cow = find_cows(cow_name)

    if cow:
        message = arguments[2:]
        message_string = ""

        for word in message:
            message_string += word + " "

        print(message_string)
        print(cow.image)

        if isinstance(cow, Dragon):
            print("This dragon can breathe fire." if cow.can_breath_fire() else "This dragon cannot breathe fire.")
    else:
        print(f"Could not find {cow_name} cow!")
else:
    message_string = ""

    for word in arguments[0:]:
        message_string += word + " "

    print(message_string)
    print(heifer_generator.get_cows()[0].image)