import datetime
 
# now = datetime.datetime.now()
# print("Current date and timee is :",now)

#today = datetime.date.today()

# print("Current date :", date)

# my_birthday = datetime.date(1998,10,27)

# print("My birthday is on ",my_birthday)

today = datetime.date.today()

ten_days = datetime.timedelta(days=10)

future_date = today + ten_days
past_date = today - ten_days

print("Future date after ten days :",future_date)
print("Past date before tendays:",past_date)