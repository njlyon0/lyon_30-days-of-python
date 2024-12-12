"""
Python `datetime` Module

Python has a 'datetime' module for handling dates/times
"""

# Import module
import datetime

# Check out available content
print(dir(datetime))

# Get date/time information
now = datetime.datetime.now()
now

# Access different parts of "now" via attributes
now.day
now.year
now.second

# Can also use certain methods
## "Timestamp" is the number of seconds since Jan. 1, 1970
now.timestamp()

# Can also use the datatime function to format integers as date/times
new_year = datetime.datetime(2025, 1, 1)
type(new_year)

# Can format strings with shorthand for time units with the "strftime" method
## More on format abbreviations here: https://strftime.org/
now_time = now.strftime("%H:%M:%S")
now_time

# Can format human-readable string dates with the "strptime" method
date_str = "1 January, 2025"
date_obj = datetime.datetime.strptime(date_str, "%d %B, %Y")
date_obj

# For simpler operations, can use the "date" function
my_date = datetime.date(2025, 1, 1)
my_date

# Or can use time objects for time w/o date
my_time = datetime.time(hour = 5, minute = 30, second = 2)
my_time

# Can do math on datetime variables to get days until / since
today = datetime.date.today()
new_year = datetime.date(2025, 1, 1)
countdown = new_year - today
print(countdown.days, "days until the new year")

# Can use "timedelta" function to get time until / since
t1 = datetime.timedelta(weeks = 8, days = 4, hours = 3, seconds = 5)
t2 = datetime.timedelta(days = 10, hours = 1, minutes = 10)
t3 = t1 - t2
t3
