from meya import Component


class AgeChecker(Component):

    def start(self):
        # read in the age, and default to `0` if invalid or missing
        age = self.db.flow.get('age') or 0
        try:
            age = int(age)
        except:
            age = 0

        # check the age
        if age >= 18:
            action = "over"
        else:
            action = "under"

        # the action determines which transition is invoked
        # note that no message is returned, just an action
        return self.respond(message=None, action=action)
