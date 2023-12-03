'''

Problem: Convert Temperature from Celsius to Fahrenheit

Write a Python function that converts a temperature from Celsius to Fahrenheit. 
The formula to convert Celsius to Fahrenheit: F = C * 9/5 + 32 , where F is Fahrenheit and C is Celsius.

'''

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

test_temperatures_celsius = [0, 100, 25, -10]

fahrenheit_temperatures = {celsius: celsius_to_fahrenheit(celsius) for celsius in test_temperatures_celsius}

print(fahrenheit_temperatures)