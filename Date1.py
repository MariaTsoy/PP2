import datetime

date1 = datetime.datetime.now()
print(date1.date())
fiveDaysBefore = date1.day - 5
date2 = datetime.date(date1.year, date1.month, fiveDaysBefore)
print(date2)
