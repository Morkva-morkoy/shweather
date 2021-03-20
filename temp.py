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
weather = three_h_forecaster.get_weather_at(tomorrow_at_midnight).temperature("celsius")["temp"]
weather1 = three_h_forecaster.get_weather_at(tomorrow_at_three_night).temperature("celsius")["temp"]
weather2 = three_h_forecaster.get_weather_at(tomorrow_at_six_morning).temperature("celsius")["temp"]
weather3 = three_h_forecaster.get_weather_at(tomorrow_at_nine_morning).temperature("celsius")["temp"]
weather4 = three_h_forecaster.get_weather_at(tomorrow_at_mid).temperature("celsius")["temp"]
weather5 = three_h_forecaster.get_weather_at(tomorrow_at_three).temperature("celsius")["temp"]
weather6 = three_h_forecaster.get_weather_at(tomorrow_at_six).temperature("celsius")["temp"]
weather7 = three_h_forecaster.get_weather_at(tomorrow_at_nine).temperature("celsius")["temp"]
<<<<<<< HEAD
weather_tomorrow = [weather, weather1, weather2, weather3, weather4, weather5, weather6, weather7]
=======
print([weather, weather1, weather2, weather3, weather4, weather6, weather7])
>>>>>>> bdac948cbca7bbb47e37677b752412409f68f277
