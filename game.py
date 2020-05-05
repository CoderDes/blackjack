from exceptions import NumberError


class Player:
    def hit(self):
        pass

    def stand(self):
        pass


class Human(Player):
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank


class Computer(Player):
    def __init__(self, name='Computer'):
        self.name = name


class Deck:
    deck_volume = 52
    suits = ['diamond', 'club', 'heart', 'spade']
    faces = ['king', 'queen', 'soldier', 'ace']
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    cards = []

    def shuffle_deck(self):
        pass

    def generate_deck(self):
        for suit in self.suits:
            for face in self.faces:
                self.cards.append(Card(face, suit))
            for number in self.numbers:
                self.cards.append(Card(number, suit))
        print('DECK', self.cards)
        print('LENGTH', len(self.cards))

    def give_card(self):
        pass


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

