import datetime

d = datetime.date(2020, 5, 18)
#print(d)

tday = datetime.date.today()
#print(tday)

#print(tday.day)

# weekday: Mon = 0 Tue = 1
#print(tday.weekday())
# isoweekday: Mon = 1 Tue = 2
#print(tday.isoweekday())


tdelta = datetime.timedelta(days=7)
#print(tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2020, 5, 27)

till_bday = bday - tday
#print(till_bday.days)
#print(till_bday.total_seconds())


t = datetime.time(9, 30, 45, 100000)
#print(t)
#print(t.hour)

'''datetime.date vs datetime.time vs datetime.datetime'''

dt = datetime.datetime(2020, 5, 18, 21, 32, 10, 100000)
#print(dt)

tdelta = datetime.timedelta(hours=3)
#print(dt + tdelta)



dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

#print(dt_today)
#print(dt_now)
#print(dt_utcnow)

import pytz

dt = datetime.datetime(2020, 5, 18, 9, 40, 10, tzinfo=pytz.UTC)
#print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

# Some will use this but utcnow does not have timezone-aware factor. NOT that good so we can use replace()
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
#print(dt_utcnow)


# take US which has more timezones
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
#print(dt_mtn)

#for tz in pytz.all_timezones:
    #print(tz)

dt_sg = dt_utcnow.astimezone(pytz.timezone('Singapore'))
#print(dt_sg)



# strftime = Datetime to String
# strptime = String to Datetime

print(dt_sg.strftime('%B %d, %Y'))

dt_str = 'May 19, 2020'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

