# math & datetime module in python
# math & datetime & json etc..
# Math module:- It is used to perform mathematical operations using math classes
# import math
# print(math.floor(16.99))
# print(math.floor(17.4))
# print(math.ceil(7.88))
# print(math.ceil(7.45))
# print(int(math.sqrt(9)))
# print(int(math.sqrt(36)))
# print(math.sqrt(7))
# inp=int(input("Enter a number:-"))
# print(math.floor(inp))
# print(math.ceil(inp))
# print(math.sqrt(inp))
# print(math.fabs(-1))
# import datetime
# # print(datetime)
# print(datetime.date(2025,9,3)-datetime.date(2003,8,13))
# print(datetime.date.today())
# Current date
# from datetime import date
# cd=date.today()
# print(cd)
# print(cd.day)
# print(cd.month)
# print(cd.year)
# Custom date
# a=date(2003,8,13)
# print(a)
# print(a.day)
# print(a.month)
# print(a.year)
# print(a.weekday())
# print(a.isoweekday()) # strictly use this for the date 
# print(a.isocalendar())
# print(a.isoformat())
# print(a.ctime())
# print(date.fromisoformat("2025-12-25"))
# from datetime import time
# t=time(14,30,33,123456)
# print(t)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)
# from datetime import datetime, timezone
# now=datetime.now()
# print(now)
# utc_date=datetime.now(timezone.utc)
# print(utc_date)
# from datetime import datetime
# import pytz
# cdt=datetime.now(pytz.UTC)
# print(cdt)
# us_t=pytz.timezone("US/eastern")
# now=datetime.now(us_t)
# print(now)
# in_t=pytz.timezone("Asia/Calcutta")
# tim_z=datetime.now(in_t)
# print(tim_z)
# abc=datetime.now()
# xyz=abc.strftime("%Y-%m-%d %H-%M-%S")
# deg=abc.strftime("%A, %B, %d, %Y")
# print(deg)
# print(xyz)