def reformat(data):
    new_data = {}

    for i in data:
        if not new_data.get(i["type"]):
                new_data[i["type"]] = {}

        new_data[i["type"]].update({i["name"]: i["price"]})
    
    return new_data


def nth(data, n):
    if data is None:
        return None

    if n % 2 == 1 and n != 0:
        return nth(data[1], n - 1)
    elif n == 0:
        return data[n]
    else:
        return nth(data[1], n - 1)

def where(data):
    count = 0

    if data == "Waldo":
        count += 1

    if type(data) is dict:
        for i in data:
            if i == "Waldo" or data[i] == "Waldo":
                count += 1

            if type(data[i]) is dict:
                count += where(data[i])
            elif type(data[i]) is list:
                count += where(data[i])
    elif type(data) is list:
        for i in range(len(data)):
            if data[i] == "Waldo":
                count += 1

            if type(data[i]) is dict:
                count += where(data[i])
            elif type(data[i]) is list:
                count += where(data[i])

    return count