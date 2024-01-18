#prints last dates of last 7 days

import datetime

today = datetime.datetime.now()

for i in range(7):
    print(today - datetime.timedelta(days=i))

