yearA = int(input("Enter the year for date 1: "))
monthA = int(input("Enter the month for date 1: "))
dayA = int(input("Enter the day for date 1: "))

yearB = int(input("Enter the year for date 2: "))
monthB = int(input("Enter the month for date 2: "))
dayB = int(input("Enter the day for date 2: "))

difference = abs(((yearB - yearA) * 360) + ((monthB - monthA) * 30) + (dayB - dayA))

print(f"The difference between {monthA}/{dayA}/{yearA} and {monthB}/{dayB}/{yearB} is {difference} days!")