from meya import Component


class PizzaConfirmation(Component):

    def start(self):
        # read the order and make lower case
        order = self.db.flow.get('pizza_type') or ""
        order = order.lower()
        print order

        # conditional
        if "anchovies" in order:
            text = "Sorry, we don't serve anchovies"
        elif "hawaiian" in order:
            text = "Are you nuts? Don't put fruit on pizza!"
        elif order:
            text = "Thanks for your order! Pizza: {}".format(order)
        else:
            text = "No order received :("

        # respond to the user
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
