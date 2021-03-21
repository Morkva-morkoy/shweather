from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('9a5b8a94e895ee75f75dee6ec42c3414')
mgr = owm.weather_manager()
observation_spb = mgr.weather_at_place("Saint Petersburg, RU")
w_spb = observation_spb.weather
v_spb = w_spb.wind()["speed"]
observation_msk = mgr.weather_at_place("Moscow, RU")
w_msk = observation_msk.weather
v_msk = w_msk.wind()["speed"]

observation_don = mgr.weather_at_place("Donetsk, UA")
w_don = observation_don.weather
v_don = w_don.wind()["speed"]

