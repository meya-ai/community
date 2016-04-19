# -*- coding: utf-8 -*-
from meya import Component


class SetShoeSize(Component):

    def start(self):
        shoe_size = self.db.request.get('shoe_size')
        self.db.user.set('shoe_size', shoe_size)
        text = "Shoe size was set to : {}".format(shoe_size)
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
