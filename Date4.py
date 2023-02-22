import datetime

date1 = datetime.datetime.now()
date2 = datetime.datetime(2023, 2, 24)
difference = (date2 - date1).total_seconds()
print(difference)
