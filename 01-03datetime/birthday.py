from datetime import datetime
from datetime import date

today = date.today()

mybirthday = date(2019, 12, 31)

if mybirthday is not today:
    print("Your birthday is still " + str((mybirthday - today).days) + " days away!")

else:
    print("It's your birthday!")