from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('9a5b8a94e895ee75f75dee6ec42c3414')
mgr = owm.weather_manager()
observation_spb = mgr.weather_at_place("Saint Petersburg, RU")
w_spb = observation_spb.weather
d_spb = w_spb.pressure["press"]
observation_msk = mgr.weather_at_place("Moscow, RU")
w_msk = observation_msk.weather
d_msk = w_msk.pressure["press"]

observation_don = mgr.weather_at_place("Donetsk, UA")
w_don = observation_don.weather
d_don = w_don.pressure["press"]
