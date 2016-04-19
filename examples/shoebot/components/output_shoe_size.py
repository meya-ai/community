# -*- coding: utf-8 -*-
from meya import Component


class OutputShoeSize(Component):

    def start(self):
        shoe_size = self.db.user.get('shoe_size')
        text = "Your shoe size is {}".format(shoe_size)
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
