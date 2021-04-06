from pyowm import OWM
from pyowm.utils import timestamps, formatting, config
import datetime

owm = OWM('9a5b8a94e895ee75f75dee6ec42c3414')
mgr = owm.weather_manager()

observation_spb = mgr.weather_at_place("Saint Petersburg, RU")
w_spb = observation_spb.weather
tem_spb = w_spb.temperature("celsius")["temp"]

observation_msk = mgr.weather_at_place("Moscow, RU")
w_msk = observation_msk.weather
tem_msk = w_msk.temperature("celsius")["temp"]

observation_don = mgr.weather_at_place("Donetsk, UA")
w_don = observation_don.weather
tem_don = w_don.temperature("celsius")["temp"]

tomorrow_at_midnight = timestamps.tomorrow(0, 0)
tomorrow_at_three_night = timestamps.tomorrow(3, 0)
tomorrow_at_six_morning = timestamps.tomorrow(6, 0)
tomorrow_at_nine_morning = timestamps.tomorrow(9, 0)
tomorrow_at_mid = timestamps.tomorrow(12, 0)
tomorrow_at_three = timestamps.tomorrow(15, 0)
tomorrow_at_six = timestamps.tomorrow(18, 0)
tomorrow_at_nine = timestamps.tomorrow(21, 0)

three_h_forecaster = mgr.forecast_at_place('Saint Petersburg', '3h')
sweather_tomorrow = three_h_forecaster.get_weather_at(tomorrow_at_midnight).temperature("celsius")["temp"]
sweather_tomorrow1 = three_h_forecaster.get_weather_at(tomorrow_at_three_night).temperature("celsius")["temp"]
sweather_tomorrow2 = three_h_forecaster.get_weather_at(tomorrow_at_six_morning).temperature("celsius")["temp"]
sweather_tomorrow3 = three_h_forecaster.get_weather_at(tomorrow_at_nine_morning).temperature("celsius")["temp"]
sweather_tomorrow4 = three_h_forecaster.get_weather_at(tomorrow_at_mid).temperature("celsius")["temp"]
sweather_tomorrow5 = three_h_forecaster.get_weather_at(tomorrow_at_three).temperature("celsius")["temp"]
sweather_tomorrow6 = three_h_forecaster.get_weather_at(tomorrow_at_six).temperature("celsius")["temp"]
sweather_tomorrow7 = three_h_forecaster.get_weather_at(tomorrow_at_nine).temperature("celsius")["temp"]

mthree_h_forecaster = mgr.forecast_at_place('Moscow', '3h')
mweather_tomorrow = mthree_h_forecaster.get_weather_at(tomorrow_at_midnight).temperature("celsius")["temp"]
mweather_tomorrow1 = mthree_h_forecaster.get_weather_at(tomorrow_at_three_night).temperature("celsius")["temp"]
mweather_tomorrow2 = mthree_h_forecaster.get_weather_at(tomorrow_at_six_morning).temperature("celsius")["temp"]
mweather_tomorrow3 = mthree_h_forecaster.get_weather_at(tomorrow_at_nine_morning).temperature("celsius")["temp"]
mweather_tomorrow4 = mthree_h_forecaster.get_weather_at(tomorrow_at_mid).temperature("celsius")["temp"]
mweather_tomorrow5 = mthree_h_forecaster.get_weather_at(tomorrow_at_three).temperature("celsius")["temp"]
mweather_tomorrow6 = mthree_h_forecaster.get_weather_at(tomorrow_at_six).temperature("celsius")["temp"]
mweather_tomorrow7 = mthree_h_forecaster.get_weather_at(tomorrow_at_nine).temperature("celsius")["temp"]

dthree_h_forecaster = mgr.forecast_at_place('Donetsk', '3h')
dweather_tomorrow = dthree_h_forecaster.get_weather_at(tomorrow_at_midnight).temperature("celsius")["temp"]
dweather_tomorrow1 = dthree_h_forecaster.get_weather_at(tomorrow_at_three_night).temperature("celsius")["temp"]
dweather_tomorrow2 = dthree_h_forecaster.get_weather_at(tomorrow_at_six_morning).temperature("celsius")["temp"]
dweather_tomorrow3 = dthree_h_forecaster.get_weather_at(tomorrow_at_nine_morning).temperature("celsius")["temp"]
dweather_tomorrow4 = dthree_h_forecaster.get_weather_at(tomorrow_at_mid).temperature("celsius")["temp"]
dweather_tomorrow5 = dthree_h_forecaster.get_weather_at(tomorrow_at_three).temperature("celsius")["temp"]
dweather_tomorrow6 = dthree_h_forecaster.get_weather_at(tomorrow_at_six).temperature("celsius")["temp"]
dweather_tomorrow7 = dthree_h_forecaster.get_weather_at(tomorrow_at_nine).temperature("celsius")["temp"]

tzinfo = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo

spb_tzinfo = datetime.timezone(datetime.timedelta(seconds=10800))
san_fran_tzinfo = datetime.timezone(datetime.timedelta(days=-1, seconds=61200))
# now = datetime.datetime.now().hour
# now_bruh = now/3
if datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo == datetime.timezone(datetime.timedelta(days=-1, seconds=61200), 'US Mountain Standard Time'):
    print("Location: San-Francisco(Heroku global server)")
    now = datetime.datetime.now().hour
    now_bruh = int(now/3)*3
    new_day = False
    spb_time_now = now_bruh+10
    if spb_time_now > 23:
        spb_time_now = spb_time_now - 24
        new_day = True
    spb_time_now = int(spb_time_now/3)*3
    now_unix = formatting.to_UNIXtime(datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, int(now_bruh)-1, 0, tzinfo=san_fran_tzinfo))
    now = spb_time_now
elif datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo == datetime.timezone(datetime.timedelta(seconds=10800), 'Russia TZ 2 Standard Time'):
    print("Location: Saint-Petersburg(Flask local server)")
    now = datetime.datetime.now().hour
    now_bruh = int(now/3)*3
    san_fran_time_now = now_bruh-10
    san_fran_time_now = int(san_fran_time_now/3)*3
    now_unix = formatting.to_UNIXtime(datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, int(now_bruh), 0, tzinfo=spb_tzinfo))

# spb_weather_now = mgr.one_call_history(lat=59.9386, lon=30.3141, dt=now_unix).current.temperature("celsius")["temp"]
# if isinstance(now_bruh, float):
#     now = int(now_bruh)*3
# else:
#     pass

# now = spb_time_now

def get_forecast(city, lat, lon):
    if new_day == True:
        day = datetime.datetime.now().day + 1
    else:
        day = datetime.datetime.now().day
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    x = 0
    n = []
    n1 = []

    while x <= now:
        n.append(x)
        x += 3

    for i in n:
        try:
            tchn = formatting.to_UNIXtime(datetime.datetime(year, month, day, i, 0, tzinfo=spb_tzinfo))
            n1.append(mgr.one_call_history(lat=lat, lon=lon, dt=tchn).current.temperature("celsius")["temp"])
        except Exception:
            pass

    three_h_forecaster = mgr.forecast_at_place(city, '3h')
    while 22 > x > now:
        n.append(x)
        n1.append(three_h_forecaster.get_weather_at(datetime.datetime(year, month, day, x, 0, tzinfo=spb_tzinfo)).temperature("celsius")["temp"])
        x += 3
    return n1

sweather_today = get_forecast("Saint Petersburg, RU", 59.9386, 30.3141)
mweather_today = get_forecast("Moscow, RU", 55.7522, 37.6156)
dweather_today = get_forecast("Donetsk, UA", 48.023, 37.8022)