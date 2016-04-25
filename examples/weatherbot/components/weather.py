import requests
from meya import Component


API_URL = (
    "http://api.openweathermap.org/data/2.5/weather"
    "?q={city},{country}&APPID={api_key}"
)
API_KEY = '0d3efb33fc57a68d3d90224751ee224d'


def farenheit(celsius):
    return 9.0/5.0 * celsius + 32


class Weather(Component):

    def start(self):
        city = self.db.flow.get('city') or \
            self.properties.get('city') or "New York"
        country = self.db.flow.get('country') or \
            self.properties.get('country') or "US"
        url = API_URL.format(city=city, country=country, api_key=API_KEY)
        data = requests.get(url).json()
        temp = int(data['main']['temp'] - 273.15)
        description = data['weather'][0]['description']

        if country == "US":
            units = "F"
            temp = farenheit(temp)
        else:
            units = "C"

        text = (
            "It is currently {temp}{units} with {description} in {city}! :D"
        ).format(
            temp=temp,
            units=units,
            description=description,
            city=city,
            country=country
        )
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
