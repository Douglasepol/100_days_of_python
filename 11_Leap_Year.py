
'''

Problem: Determine if a Year is a Leap Year

Write a Python function that takes a year as input and returns True if the year is a leap year, and False otherwise. 

A leap year is defined as follows:
	It is divisible by 4.
	However, if the year is divisible by 100, it is not a leap year, unless...
	The year is also divisible by 400. Then it is a leap year.

'''

def is_leap_year(year):
    # Check if the year is a leap year
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

test_years = [2000, 1900, 2012, 2100, 2400]
leap_year_results = {}

for year in test_years:
    leap_year_results[year] = is_leap_year(year)

print(leap_year_results)