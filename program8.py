# Write a Python programm to display the calendar:

import calendar

year = int(input("Enter year: ")) 
month = int(input("Enter month (1-12): "))

cal = calendar.month(year, month)

print(cal)