import random

from card import Card


class Deck:
    suits = ['diamond', 'club', 'heart', 'spade']
    faces = ['king', 'queen', 'soldier', 'ace']
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    cards = []

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def generate_deck(self):
        for suit in self.suits:
            for face in self.faces:
                self.cards.append(Card(face, suit))
            for number in self.numbers:
                self.cards.append(Card(number, suit))

    def give_card(self):
        pass
