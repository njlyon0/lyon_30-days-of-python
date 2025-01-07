# Exercises - Date/Times

## Import module
import datetime

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.datetime.now()
now.day
now.month
now.year
now.hour
now.minute
now.timestamp()

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
now_reformat = now.strftime("%m/%d/%Y, %H:%M:%S")
now_reformat

# 3. Today is 5 December, 2019. Change this time string to time.
date_var = datetime.datetime.strptime("5 December, 2019", "%d %B, %Y")
date_var

# 4. Calculate the time difference between now and new year.
new_year_diff =  datetime.datetime(year = 2025, month = 1, day = 1) - now
new_year_diff.days

# 5. Calculate the time difference between 1 January 1970 and now.
jan_seventy = datetime.datetime(1970, 1, 1)
time_since = now - jan_seventy
time_since

# 6. Think, what can you use the datetime module for? (E.g., time series analysis, get a timestamp of any activities in an application, adding posts on a blog, etc.)


