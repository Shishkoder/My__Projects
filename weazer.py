from colorama import init
from colorama import Fore, Back, Style

init()

import pyowm

owm = pyowm.OWM( '6254c4f36ab454536b5c0ba0bf1b7d75', language = "ru" )

print( Back.YELLOW )
print( Fore.RED )

place = input( "Введите город: " )

observation = owm.weather_at_place( place )
w = observation.get_weather()

speed = w.get_wind()['speed']
hum = w.get_humidity()
temp = w.get_temperature('celsius')['temp']

print( Back.CYAN )
print( Fore.BLACK )

print( "В городе " + place + " сейчас " + w.get_detailed_status() )
print( "Температура сейчас в районе " + str( temp ) + " °C, " + str( hum ) + " осадков, " + str( speed ) + " скорость ветра." )  

print( Back.YELLOW )
print( Fore.BLACK )

if temp < 10:
	print( "На улице холодно, лучше одеться, тебе так не кажется?" )
elif temp < 20:
	print (Back.GREEN)
	print (Fore.BLACK)

	print ( "Вроде на улице не так холодно, но стоит одеться потеплее." )
else:

	print (Back.MAGENTA)
	print (Fore.BLACK)

	print ( "Тепло, давай хоть в сланцах и шортах!")

input()
