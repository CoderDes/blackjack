from exceptions import NumberError


class Card:
    card_values = {
        'king': 4,
        'queen': 3,
        'soldier': 2,
        'ace': None,
    }

    def __init__(self, name, suit):
        self.name = f'{name} {suit}'
        self.card_value = self.define_value(name)

    def define_value(self, card_name):
        # TODO: Check with type(card_name) == int
        if isinstance(card_name, int):
            return int(card_name)
        return self.card_values[card_name]

    def ace_define(self):
        try:
            ace_value = int(input('11 or 1? '))
            if ace_value != 11 or ace_value != 1:
                raise NumberError('Wrong number!', 'Please, enter 11 or 1.')
            ace = ace_value
        except TypeError:
            print('You entered not a number. Please, try again.')
            self.ace_define()
        except NumberError:
            self.ace_define()
        except:
            print('Something went wrong. Try again.')
