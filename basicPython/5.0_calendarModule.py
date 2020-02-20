# Write a Python program to print the calendar of a given month and year. Note : Use 'calendar' module.
import calendar
class Calandar:
    def Cal(self,year=1994,month=2):
        print("calendar")
        print(calendar.month(year,month))

year=2020
month=2
cale=Calandar()
cale.Cal(year,month)
