#Then month_dates.py custom code is
import calendar
import datetime

def month_dates():
   now = datetime.datetime.now()
   print(calendar.monthrange(now.year,now.month)[1])
   return calendar.monthrange(now.year, now.month)[1]




month_dates()