from sys import int_info

initial_unit = input("Enter the unit you are converting from: ")
final_unit = input("Enter the unit you are converting to: ")
temperature = float(input(f"Enter the temperature in {initial_unit}: "))

fahrenheit_to_celsius = (temperature - 32) * 5/9
celsius_to_fahrenheit = (temperature * 9/5) + 32
fahrenheit_to_kelvin = (temperature - 32) * 5/9 + 273.15
kelvin_to_fahrenheit = (temperature - 273.15) * 9/5 + 32
celsius_to_kelvin = temperature + 273.15
kelvin_to_celsius = temperature - 273.15

final_answer = ""

if initial_unit == "Kelvin":
    if final_unit == "Celsius":
        final_answer = kelvin_to_celsius
    elif final_unit == ("Fahrenheit"):
        final_answer = kelvin_to_fahrenheit
    else:
        final_answer = temperature
elif initial_unit == "Fahrenheit":
    if final_unit == "Celsius":
        final_answer = fahrenheit_to_celsius
    elif final_unit == "Kelvin":
        final_answer = fahrenheit_to_kelvin
    else:
        final_answer = temperature
elif initial_unit == "Celsius":
    if final_unit == "Fahrenheit":
        final_answer = celsius_to_fahrenheit
    elif final_unit == "Kelvin":
        final_answer = celsius_to_kelvin
    else:
        final_answer = temperature

print(f"That is {final_answer:.1f} degrees {final_unit}.")