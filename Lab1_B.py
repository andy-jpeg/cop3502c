item_price = float(input("Enter the price of the item: "))
sales_tax = 1 + (float(input("Enter the sales tax percentage: ")) / 100)

total_price = item_price * sales_tax
print(f"Your total is ${total_price:.2f}")