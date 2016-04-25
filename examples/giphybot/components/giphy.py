from meya import Component
import requests

API_KEY = "dc6zaTOxFJmzC"
API_URL = "http://api.giphy.com/v1/gifs/random?tag={tag}&api_key={key}"


class Giphy(Component):
    """Outputs a random giphy url based on passed in tag as either
    a property or flow db"""

    def start(self):
        tag = self.properties.get('tag') or \
            self.db.flow.get('tag') or "funny"

        response = requests.get(API_URL.format(tag=tag, key=API_KEY))
        gif = response.json()['data']['url']

        message = self.create_message(text=gif)

        return self.respond(message=message, action="next")
