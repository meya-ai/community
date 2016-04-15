# -*- coding: utf-8 -*-
import requests
from meya import Component


class IFTTT(Component):

    def start(self):
        event = self.properties.get('event')
        key = self.properties.get('key')
        url = "https://maker.ifttt.com/trigger/{event}/with/key/{key}"
        url = url.format(event=event, key=key)
        data = {
            'value1': self.db.request.get('value1'),
            'value2': self.db.request.get('value2'),
            'value3': self.db.request.get('value3')
        }
        response = requests.post(
            url=url,
            json=data)
        print response.text
        return self.respond(message=None, action="next")
