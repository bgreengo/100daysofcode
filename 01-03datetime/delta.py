from datetime import datetime
from datetime import timedelta

eta = timedelta(hours=6)

today = datetime.today()

print("In 6 hours it will be " + str(today + eta))