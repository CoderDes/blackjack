import random

from bank import Bank
from player import Player
from deck import Deck
from card import Card
from hand import Hand


class Human(Player):
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.cards = {}


class Dealer(Player):
    def __init__(self, name='Dealer'):
        self.name = name
        self.cards = {}

    def show_first_card(self):
        random_card = self.cards.popitem()
        random_card = {random_card[0]: random_card[1]}
        return self.show_cards(random_card)


deck = Deck()
deck.generate_deck()
deck.shuffle_deck()

human = Human('Jason', 100)
dealer = Dealer()

bank = Bank()
bank.ask_bet(human)

hand = Hand(deck.cards, [human, dealer])
hand.give_initial_cards(human, dealer)

print(dealer.show_first_card())
print(human.show_cards(human.cards))

hand.ask_player(human)
