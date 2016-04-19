# -*- coding: utf-8 -*-
from meya import Component


class CheckShoeSize(Component):

    def start(self):
        shoe_size = self.db.user.get('shoe_size')
        if shoe_size:
            action = "exists"
        else:
            action = "doesnt"
        return self.respond(message=None, action=action)
