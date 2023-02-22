import datetime

today = datetime.datetime.now()
oneDayBefore = today.day - 1
oneDayAfter = today.day + 1
yesterday = datetime.date(today.year, today.month, oneDayBefore)
tomorrow = datetime.date(today.year, today.month, oneDayAfter)
print("Yesterday: ", yesterday)
print("Today: ", today.date())
print("Tomorrow: ", tomorrow)
