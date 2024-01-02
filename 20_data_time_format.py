'''
Problem: Display Current Date and Time Information

This Python program displays various pieces of information about the current date and time. It uses the datetime module to access and format date and time data. The program outputs:
- The current date and time.
- The current year.
- The name of the current month.
- The week number of the current year.
- The weekday number (where Sunday is 0 and Saturday is 6).
- The day number of the year.
- The day number of the month.
- The name of the current weekday.

'''

import time
import datetime

print("Current date and time: " , datetime.datetime.now())
print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))
