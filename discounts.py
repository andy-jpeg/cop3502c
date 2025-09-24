price = float(input("Enter the price: "))
coupon1 = input("Is it black friday [y/n]: ")
coupon2 = input("Do you have a coupon [y/n]: ")
coupon3 = input("Do you have an employee discount [y/n]: ")

if coupon1 == "y": # Black Friday coupon
    price *= 0.6
if coupon2 == "y": # One's own coupon
    price *= 0.95
if coupon3 == "y": # Employee discount
    price *= 0.8

print(f"The final price is: ${price:.2f}")