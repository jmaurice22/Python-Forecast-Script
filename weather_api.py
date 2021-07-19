# Imports
import requests, json, math

degree_sign = u"\N{DEGREE SIGN}"

# API KEY
api_key = 'f0d6ab958d9c3097d6dcbaf7427c4ec4'
# BASE URL
base_url = 'https://api.openweathermap.org/data/2.5/weather?'
#GET CITY INPUT FROM USER
city = str(input('Enter City Name: '))
#FULL URL
full_url = base_url + 'q=' + city + '&' + 'units=imperial' + '&appid='+ api_key

# REQUEST TO SERVER
response = requests.get(full_url)


#check for successlfu response *code 200*
if response.status_code == 200:
    data = response.json()
    main = data['main']
    temp = main['temp']
    feels_like = main['feels_like']
    temp_max = main['temp_max']
    pressure = main['pressure']
    humidity = main['humidity']

    #PRINT OUTPUT TO TERMINAL
    print('Current Temperature: ' + str(round(temp)) + "" + degree_sign + "F" )
    print('Feels Like: ' + str(round(feels_like)) + "" + degree_sign + "F")
    print('High today of: ' + str(round(temp_max)) + "" + degree_sign + "F")
    print('Pressure: ' + str(round(pressure)) + " inHG")
    print('Humidity: ' + str(round(humidity)) + "%")

else:
    #ERROR HANDLING
    print('Error: Weather Data Not Found 😕')