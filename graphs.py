from temp import weather_tomorrow
from matplotlib import pyplot as plt
import datetime

x = [9, 12, 15, 18, 21]
y = weather_tomorrow

current_month = int(datetime.datetime.now().month)
current_date = int(datetime.datetime.now().day)

months_list = ["bruh", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

plt.plot(x, y)
plt.xlabel("Daytime")
plt.ylabel("Temperature(celsius)")
plt.title(f"Weather forecast for {months_list[current_month]}, {current_date+1}")
plt.savefig("bruh.png")
plt.show()