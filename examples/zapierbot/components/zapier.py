# -*- coding: utf-8 -*-
import requests
from meya import Component


class Zapier(Component):

    def start(self):
        url = self.properties.get('webhook')
        data = {
            'name': self.db.flow.get('name'),
            'os': self.db.flow.get('os'),
            'email': self.db.flow.get('email')
        }
        response = requests.post(
            url=url,
            json=data)
        print response.json()

        return self.respond(message=None, action="next")
