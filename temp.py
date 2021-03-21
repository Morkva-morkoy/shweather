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

observation_don = mgr.weather_at_place("Kropyvnytskyi, UA")
w_kro = observation_don.weather
tem_kro = w_kro.temperature("celsius")["temp"]
# three_h_forecast = mgr.forecast_at_place('Saint Petersburg, RU', '3h').forecast
# print(forecaster.when_starts('iso'))
# print(forecaster.when_ends('iso'))

three_h_forecaster = mgr.forecast_at_place('Saint Petersburg', '3h')
tomorrow_at_midnight = timestamps.tomorrow(0, 0)
tomorrow_at_three_night = timestamps.tomorrow(3, 0)
tomorrow_at_six_morning = timestamps.tomorrow(6, 0)
tomorrow_at_nine_morning = timestamps.tomorrow(9, 0)
tomorrow_at_mid = timestamps.tomorrow(12, 0)
tomorrow_at_three = timestamps.tomorrow(15, 0)
tomorrow_at_six = timestamps.tomorrow(18, 0)
tomorrow_at_nine = timestamps.tomorrow(21, 0)
sweather = three_h_forecaster.get_weather_at(tomorrow_at_midnight).temperature("celsius")["temp"]
sweather1 = three_h_forecaster.get_weather_at(tomorrow_at_three_night).temperature("celsius")["temp"]
sweather2 = three_h_forecaster.get_weather_at(tomorrow_at_six_morning).temperature("celsius")["temp"]
sweather3 = three_h_forecaster.get_weather_at(tomorrow_at_nine_morning).temperature("celsius")["temp"]
sweather4 = three_h_forecaster.get_weather_at(tomorrow_at_mid).temperature("celsius")["temp"]
sweather5 = three_h_forecaster.get_weather_at(tomorrow_at_three).temperature("celsius")["temp"]
sweather6 = three_h_forecaster.get_weather_at(tomorrow_at_six).temperature("celsius")["temp"]
sweather7 = three_h_forecaster.get_weather_at(tomorrow_at_nine).temperature("celsius")["temp"]
mthree_h_forecaster = mgr.forecast_at_place('Moscow', '3h')
mweather = mthree_h_forecaster.get_weather_at(tomorrow_at_midnight).temperature("celsius")["temp"]
mweather1 = mthree_h_forecaster.get_weather_at(tomorrow_at_three_night).temperature("celsius")["temp"]
mweather2 = mthree_h_forecaster.get_weather_at(tomorrow_at_six_morning).temperature("celsius")["temp"]
mweather3 = mthree_h_forecaster.get_weather_at(tomorrow_at_nine_morning).temperature("celsius")["temp"]
mweather4 = mthree_h_forecaster.get_weather_at(tomorrow_at_mid).temperature("celsius")["temp"]
mweather5 = mthree_h_forecaster.get_weather_at(tomorrow_at_three).temperature("celsius")["temp"]
mweather6 = mthree_h_forecaster.get_weather_at(tomorrow_at_six).temperature("celsius")["temp"]
mweather7 = mthree_h_forecaster.get_weather_at(tomorrow_at_nine).temperature("celsius")["temp"]
dthree_h_forecaster = mgr.forecast_at_place('Donetsk', '3h')
dweather = dthree_h_forecaster.get_weather_at(tomorrow_at_midnight).temperature("celsius")["temp"]
dweather1 = dthree_h_forecaster.get_weather_at(tomorrow_at_three_night).temperature("celsius")["temp"]
dweather2 = dthree_h_forecaster.get_weather_at(tomorrow_at_six_morning).temperature("celsius")["temp"]
dweather3 = dthree_h_forecaster.get_weather_at(tomorrow_at_nine_morning).temperature("celsius")["temp"]
dweather4 = dthree_h_forecaster.get_weather_at(tomorrow_at_mid).temperature("celsius")["temp"]
dweather5 = dthree_h_forecaster.get_weather_at(tomorrow_at_three).temperature("celsius")["temp"]
dweather6 = dthree_h_forecaster.get_weather_at(tomorrow_at_six).temperature("celsius")["temp"]
dweather7 = dthree_h_forecaster.get_weather_at(tomorrow_at_nine).temperature("celsius")["temp"]
kthree_h_forecaster = mgr.forecast_at_place('Kropyvnytskyi', '3h')
kweather = kthree_h_forecaster.get_weather_at(tomorrow_at_midnight).temperature("celsius")["temp"]
kweather1 = kthree_h_forecaster.get_weather_at(tomorrow_at_three_night).temperature("celsius")["temp"]
kweather2 = kthree_h_forecaster.get_weather_at(tomorrow_at_six_morning).temperature("celsius")["temp"]
kweather3 = kthree_h_forecaster.get_weather_at(tomorrow_at_nine_morning).temperature("celsius")["temp"]
kweather4 = kthree_h_forecaster.get_weather_at(tomorrow_at_mid).temperature("celsius")["temp"]
kweather5 = kthree_h_forecaster.get_weather_at(tomorrow_at_three).temperature("celsius")["temp"]
kweather6 = kthree_h_forecaster.get_weather_at(tomorrow_at_six).temperature("celsius")["temp"]
kweather7 = kthree_h_forecaster.get_weather_at(tomorrow_at_nine).temperature("celsius")["temp"]