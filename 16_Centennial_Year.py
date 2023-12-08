'''
Problem: Calculate the Year When Someone Turns 100

Given a person's name, age, and birth month and day, calculate the year when they will turn 100 years old.

Parameters:
name (str): The name of the person.
age (int): The current age of the person.
birth_month (int): The birth month of the person.
birth_day (int): The birth day of the person.

Returns:
str: A message stating the year when the person will turn 100.
'''

import datetime

# Get the current date from the system
current_date = datetime.datetime.now()
current_year = current_date.year
current_month = current_date.month
current_day = current_date.day

def calculate_centennial_year(name, age, birth_month, birth_day):
    year_100 = current_year + 100 - age
    if birth_month > current_month or (birth_month == current_month and birth_day > current_day):
        year_100 -= 1
    return f"Dear {name}, you will turn 100 in the year {year_100}."

# Test examples
test_cases = [
    {"name": "Alice", "age": 30, "birth_month": 5, "birth_day": 15},
    {"name": "Bob", "age": 40, "birth_month": 1, "birth_day": 20},
    {"name": "Charlie", "age": 25, "birth_month": 2, "birth_day": 21}
]

# Iterate through each test case and calculate the year of the 100th birthday
for case in test_cases:
    message = calculate_centennial_year(case["name"], case["age"], case["birth_month"], case["birth_day"])
    print(message)
