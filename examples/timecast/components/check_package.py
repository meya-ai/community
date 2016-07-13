# -*- coding: utf-8 -*-
from meya import Component
from meya.cards import TextWithButtons, Button


class CheckPackage(Component):

    def start(self):
        # TODO: get this information from the fictional Timecast API
        text = (
            "I see you're on our Basic package. I can upgrade you to Gold for "
            "$20/mo or VIP for an additional $40/mo. Are you interested in "
            "one of these upgrades? Or can I help in some other way?"
        )
        buttons = [
            Button(text='Upgrade to Gold'),
            Button(text='Upgrade to VIP')
        ]
        card = TextWithButtons(text=text, buttons=buttons)
        message = self.create_message(card=card)
        return self.respond(message=message, action="next")
