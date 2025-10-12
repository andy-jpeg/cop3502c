def parse_student(info):
    infoDict = {}

    infoDict["id"] = int(info[:8])
    infoDict["name"] = info[8:-4]
    infoDict["birthdate"] = f"{info[-4:-2]}/{info[-2:]}"

    return infoDict

def count_items(info):
    count = {}

    for value in info:
        if count.get(value, False):
            count[value] += 1
        else:
            count[value] = 1

    return count

def list_fighters(info):
    fighter_list = set()
    
    for fighter in info:
        for battle in info[fighter]:
            for fighter2 in info[fighter][battle]:
                fighter_list.add(fighter2)
        fighter_list.add(fighter)

    return sorted(fighter_list)