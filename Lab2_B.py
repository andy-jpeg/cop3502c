total_income = float(input("Enter your total income this year: "))
taxed_income = 0
nested_income = 0

if total_income <= 11600:
    taxed_income = total_income * 0.1
elif total_income <= 47150:
    nested_income = 11600 * 0.1
    taxed_income = nested_income + ((total_income - 11600) * 0.12)
elif total_income <= 100525:
    nested_income = (11600 * 0.1) + ((47150 - 11600) * 0.12)
    taxed_income = nested_income + ((total_income - 47150) * 0.22)
elif total_income <= 191950:
    nested_income = (11600 * 0.1) + ((47150 - 11600) * 0.12) + ((100525 - 47150) * 0.22)
    taxed_income = nested_income + ((total_income - 100525) * 0.24)
elif total_income <= 243725:
    nested_income = (11600 * 0.1) + ((47150 - 11600) * 0.12) + ((100525 - 47150) * 0.22) + ((191950 - 100525) * 0.24)
    taxed_income = nested_income + ((total_income - 191950) * 0.32)
elif total_income <= 609350:
    nested_income = (11600 * 0.1) + ((47150 - 11600) * 0.12) + ((100525 - 47150) * 0.22) + ((191950 - 100525) * 0.24) + ((243725 - 191950) * 0.32)
    taxed_income = nested_income + ((total_income - 243725) * 0.35)
else:
    nested_income = (11600 * 0.1) + ((47150 - 11600) * 0.12) + ((100525 - 47150) * 0.22) + ((191950 - 100525) * 0.24) + ((243725 - 191950) * 0.32) + ((609350 - 243725) * 0.35)
    taxed_income = nested_income + ((total_income - 609350) * 0.37)

print(f"You owe ${taxed_income:.2f} this year.")