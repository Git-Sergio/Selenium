import pyowm

city = input("Misto:")


owm = pyowm.OWM('dad12bb47b731ab11ef9b3959a731c75')
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature(('celsius')['temp'])

print("V misti " + city + "temperatura " + str(temperature))
print('A takoz v misti' + w.get_detailed_status())