from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
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


# today_at_midnight = datetime.datetime(2021, 3, 22, 0, 0, tzinfo=datetime.timezone.utc)
# today_at_three_night = datetime.datetime(2021, 3, 22, 3, 0, tzinfo=datetime.timezone.utc)
# today_at_six_morning = datetime.datetime(2021, 3, 22, 6, 0, tzinfo=datetime.timezone.utc)
# today_at_nine_morning = datetime.datetime(2021, 3, 22, 9, 0, tzinfo=datetime.timezone.utc)
today_at_mid = datetime.datetime(2021, 3, 22, 12, 0, tzinfo=datetime.timezone.utc)
today_at_three = datetime.datetime(2021, 3, 22, 15, 0, tzinfo=datetime.timezone.utc)
today_at_six = datetime.datetime(2021, 3, 22, 18, 0, tzinfo=datetime.timezone.utc)
today_at_nine = datetime.datetime(2021, 3, 22, 21, 0, tzinfo=datetime.timezone.utc)

tomorrow_at_midnight = timestamps.tomorrow(0, 0)
tomorrow_at_three_night = timestamps.tomorrow(3, 0)
tomorrow_at_six_morning = timestamps.tomorrow(6, 0)
tomorrow_at_nine_morning = timestamps.tomorrow(9, 0)
tomorrow_at_mid = timestamps.tomorrow(12, 0)
tomorrow_at_three = timestamps.tomorrow(15, 0)
tomorrow_at_six = timestamps.tomorrow(18, 0)
tomorrow_at_nine = timestamps.tomorrow(21, 0)

three_h_forecaster = mgr.forecast_at_place('Saint Petersburg', '3h')
sweather_today = three_h_forecaster.get_weather_at(today_at_mid).temperature("celsius")["temp"]
sweather_today1 = three_h_forecaster.get_weather_at(today_at_three).temperature("celsius")["temp"]
sweather_today2 = three_h_forecaster.get_weather_at(today_at_six).temperature("celsius")["temp"]
sweather_today3 = three_h_forecaster.get_weather_at(today_at_nine).temperature("celsius")["temp"]

sweather_tomorrow = three_h_forecaster.get_weather_at(tomorrow_at_midnight).temperature("celsius")["temp"]
sweather_tomorrow1 = three_h_forecaster.get_weather_at(tomorrow_at_three_night).temperature("celsius")["temp"]
sweather_tomorrow2 = three_h_forecaster.get_weather_at(tomorrow_at_six_morning).temperature("celsius")["temp"]
sweather_tomorrow3 = three_h_forecaster.get_weather_at(tomorrow_at_nine_morning).temperature("celsius")["temp"]
sweather_tomorrow4 = three_h_forecaster.get_weather_at(tomorrow_at_mid).temperature("celsius")["temp"]
sweather_tomorrow5 = three_h_forecaster.get_weather_at(tomorrow_at_three).temperature("celsius")["temp"]
sweather_tomorrow6 = three_h_forecaster.get_weather_at(tomorrow_at_six).temperature("celsius")["temp"]
sweather_tomorrow7 = three_h_forecaster.get_weather_at(tomorrow_at_nine).temperature("celsius")["temp"]

mthree_h_forecaster = mgr.forecast_at_place('Moscow', '3h')
mweather_today = mthree_h_forecaster.get_weather_at(today_at_mid).temperature("celsius")["temp"]
mweather_today1 = mthree_h_forecaster.get_weather_at(today_at_three).temperature("celsius")["temp"]
mweather_today2 = mthree_h_forecaster.get_weather_at(today_at_six).temperature("celsius")["temp"]
mweather_today3 = mthree_h_forecaster.get_weather_at(today_at_nine).temperature("celsius")["temp"]

mweather_tomorrow = mthree_h_forecaster.get_weather_at(tomorrow_at_midnight).temperature("celsius")["temp"]
mweather_tomorrow1 = mthree_h_forecaster.get_weather_at(tomorrow_at_three_night).temperature("celsius")["temp"]
mweather_tomorrow2 = mthree_h_forecaster.get_weather_at(tomorrow_at_six_morning).temperature("celsius")["temp"]
mweather_tomorrow3 = mthree_h_forecaster.get_weather_at(tomorrow_at_nine_morning).temperature("celsius")["temp"]
mweather_tomorrow4 = mthree_h_forecaster.get_weather_at(tomorrow_at_mid).temperature("celsius")["temp"]
mweather_tomorrow5 = mthree_h_forecaster.get_weather_at(tomorrow_at_three).temperature("celsius")["temp"]
mweather_tomorrow6 = mthree_h_forecaster.get_weather_at(tomorrow_at_six).temperature("celsius")["temp"]
mweather_tomorrow7 = mthree_h_forecaster.get_weather_at(tomorrow_at_nine).temperature("celsius")["temp"]

dthree_h_forecaster = mgr.forecast_at_place('Donetsk', '3h')
dweather_today = dthree_h_forecaster.get_weather_at(today_at_mid).temperature("celsius")["temp"]
dweather_today1 = dthree_h_forecaster.get_weather_at(today_at_three).temperature("celsius")["temp"]
dweather_today2 = dthree_h_forecaster.get_weather_at(today_at_six).temperature("celsius")["temp"]
dweather_today3 = dthree_h_forecaster.get_weather_at(today_at_nine).temperature("celsius")["temp"]

dweather_tomorrow = dthree_h_forecaster.get_weather_at(tomorrow_at_midnight).temperature("celsius")["temp"]
dweather_tomorrow1 = dthree_h_forecaster.get_weather_at(tomorrow_at_three_night).temperature("celsius")["temp"]
dweather_tomorrow2 = dthree_h_forecaster.get_weather_at(tomorrow_at_six_morning).temperature("celsius")["temp"]
dweather_tomorrow3 = dthree_h_forecaster.get_weather_at(tomorrow_at_nine_morning).temperature("celsius")["temp"]
dweather_tomorrow4 = dthree_h_forecaster.get_weather_at(tomorrow_at_mid).temperature("celsius")["temp"]
dweather_tomorrow5 = dthree_h_forecaster.get_weather_at(tomorrow_at_three).temperature("celsius")["temp"]
dweather_tomorrow6 = dthree_h_forecaster.get_weather_at(tomorrow_at_six).temperature("celsius")["temp"]
dweather_tomorrow7 = dthree_h_forecaster.get_weather_at(tomorrow_at_nine).temperature("celsius")["temp"]