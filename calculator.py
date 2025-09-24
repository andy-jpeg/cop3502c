operator = input("Enter the operation: ")
operand1 = float(input("Enter the first operand: "))
operand2 = float(input("Enter the second operand: "))

if operator == "add":
    result = operand1 + operand2
elif operator == "sub":
    result = operand1 - operand2
elif operator == "mul":
    result = operand1 * operand2
else: # division
    result = round(operand1 / operand2, 2)

print(f"Result is {result}")