money = int(input("How much money do you have: "))
candy_bars = 0
bogo = 0

total = 0

while money >= 4:
    money -= 4
    candy_bars += 1
total += candy_bars

while candy_bars >= 3:
    candy_bars -= 3
    candy_bars += 1
    bogo += 1
total += bogo

print(f"You can purchase {total} candy bars!")