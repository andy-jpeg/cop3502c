def print_backwards(data):
    counter = len(data) - 1

    if counter >= 0:
        print(data[counter], end="")
        print_backwards(data[:counter])

def format_names(data):
    new_data = []
    counter = 0

    if counter < len(data):
        new_data.append(data[counter] if data[counter].find(",") > 0 else (data[counter].split(" ")[1] + ", " + data[counter].split(" ")[0]))
        counter += 1
        
        new_data += format_names(data[counter:])
    
    return new_data

def sum_a(data):
    sum = 0

    for dict in data:
        for letter, num in dict.items():
            if letter == "a":
                sum += num

    return sum

def process_list(data):
    even_nums = []
    odd_nums = []

    for index, num in enumerate(data):
        if index % 2 == 0:
            even_nums.append(str(num))
        else:
            odd_nums.append(num * 10)


    return even_nums + odd_nums