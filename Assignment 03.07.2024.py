#using this code we gonna find the day of the week  
import datetime
date=3
month=7
year=2024
date = datetime.date(year, month, date)
day = date.strftime("%d,%m,%Y,%A")

print(day)
