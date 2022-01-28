import requests

class City(object):
    def __init__(self: any, obj: dict):
        # location
        loc = obj['location']
        self.name = loc['name']
        self.country = loc['country']
        self.lat, self.lon = loc['lat'], loc['lon']
        self.localtime = loc['localtime']

        # current
        cur = obj['current']
        self.temp = {'c': cur['temp_c'], 'f': cur['temp_f']}
        self.weather = cur['condition']['text']
        self.wind = {'kph': cur['wind_kph'], 'mph': cur['wind_mph']}
        self.feelslike = {'c': cur['feelslike_c'], 'f': cur['feelslike_f']}

url = "https://weatherapi-com.p.rapidapi.com/current.json"

search_for = input("Search for: ")
print(f'Searching for {search_for}...')

params = { "q": search_for }

headers = {
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
    'x-rapidapi-key': "e116947380msh9a4516bd0a1d5e1p1b2a00jsn19e2c1cc7cf5"
}

r = requests.get(url, headers=headers, params=params)
r = r.json()

city = City(r)

print(f'\n\nCountry: {city.country}\nCity name: {city.name}\nLocal time: {city.localtime}\nWeather: {city.weather}\nTemperature:\n  C: {city.temp["c"]}\n  F: {city.temp["f"]}\nWind:\n  Km/h: {city.wind["kph"]}\n  Mp/h: {city.wind["mph"]}')
# print(city.__dict__)