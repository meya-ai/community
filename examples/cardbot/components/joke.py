import requests
from meya import Component
from meya.cards import Card, Cards, Button


class ChuckNorrisJoke(Component):

    def start(self):
        """This demonstrates the use of a multi card reading data from
        an external datasource and then using various button types to
        transition to different states, flows, websites"""

        titles = [
            "Norris Joke #1",
            "Norris Joke #2"
        ]
        jokes = [
            self.get_joke(),
            self.get_joke()
        ]
        images = [
            "http://i.imgur.com/3jLvQ78.jpg",
            "http://i.imgur.com/6JADDnQ.jpg"
        ]
        # I'll test the three buttons types: link, transition, start
        # What's nice is that any of this data can be obtained programmatically
        # or via API
        buttons = [
            [
                Button(text="Learn", url="https://en.wikipedia.org"),
                Button(text="Next", action="next1"),
                Button(text="GO!", flow="cardbot_bonus", data={'foo': "bar1"})
            ],
            [
                Button(text="Fun", url="https://www.reddit.com"),
                Button(text="Next", action="next2", data={'ok': True}),
                Button(text="GO!", flow="cardbot_bonus", data={'foo': "bar2"})
            ]
        ]
        # construct a list of cards (they are `generic` template in Messenger)
        elements = []
        for x in range(2):
            element = Card(
                title=titles[x], text=jokes[x], image_url=images[x],
                buttons=buttons[x]
            )
            elements.append(element)

        # `Cards` is a multi card element in Messenger
        card = Cards(elements=elements)

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=card)

        # respond as you normally would
        return self.respond(message=message)

    def get_joke(self):
        response = requests.get("http://api.icndb.com/jokes/random")
        return response.json()['value']['joke']
