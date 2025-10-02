def bin(decimal):
    remainders = []
    
    while decimal >= 1:
        remainders.append(decimal % 2)
        decimal //= 2

    if len(remainders) == 0:
        return 0
    else:
        newNum = ""

        for i in reversed(remainders):
            newNum += str(i)

        return int(newNum)
        

def capitalize(string):
    string = string.split(" ")

    index = 0
    newString = ""

    for part in string:
        bits = part.lower()
        bit = bits[0]

        if bit == bits[0]:
            if bit == "o" or bit == "u" or bit == "s" or bit == "n" or bit == "d":
                bit = bits[0].lower() + bits[1:]
            else:
                bit = bits[0].upper() + bits[1:]

        if index == len(bits):
            newString += bit
        else:
            newString += bit + " "
        
        index += 1

    return newString

def partition(list, divisor):
    totalList = []
    originalList = []

    for i in range(len(list)):
        originalList.append(list[i])

        if len(originalList) == divisor:
            totalList.append(originalList)
            originalList = []
        elif list[i] == list[-1]:
            totalList.append(originalList)

    return totalList