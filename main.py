import datetime
import time

#datetime object
dt = datetime.datetime.now()
a=0
print("Datetime object =", dt)

# printing in dd/mm/YY H:M:S format using strftime()

print(dt.strftime("%H:%M:%S"))
time.sleep(3)

print(float(datetime.datetime.now().strftime("%H:%M:%S")) - float(dt.strftime("%H:%M:%S")))
