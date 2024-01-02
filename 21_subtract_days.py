'''
Problem: Display Current Date and 5 Days Prior

This Python script calculates and displays the current date and the date 5 days before the current date. It utilizes the datetime module, specifically the date and timedelta classes, to perform date manipulation. The program:
- Imports the date and timedelta classes from the datetime module.
- Calculates the date 5 days before today using timedelta.
- Prints the current date.
- Prints the date that is 5 days before the current date.

Outputs:
- The script outputs the current date and the date 5 days prior to the console.
'''
from datetime import date, timedelta
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)
