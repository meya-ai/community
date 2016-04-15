# -*- coding: utf-8 -*-
import requests
from meya import Component


class Zapier(Component):

    def start(self):
        url = self.properties.get('webhook') or self.db.request.get('webhook')
        data = {
            'name': self.db.request.get('name'),
            'os': self.db.request.get('os'),
            'email': self.db.request.get('email')
        }
        response = requests.post(
            url=url,
            json=data)
        print response.json()

        return self.respond(message=None, action="next")
