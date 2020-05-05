class NumberError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class NotEnoughtFunds(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
