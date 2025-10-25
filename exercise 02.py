# time module is imported to get the current hour and minute
import time
hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
if hour < 12 and minute < 00:
    print("Good morning!")
elif hour < 18 and minute < 00:
    print("Good afternoon!")
else:
    print("Good night!")