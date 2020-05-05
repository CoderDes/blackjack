from bank import Bank
from player import Player
from deck import Deck
from card import Card
from hand import Hand


class Human(Player):
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.cards = []


class Computer(Player):
    def __init__(self, name='Computer'):
        self.name = name
        self.cards = []


deck = Deck()
deck.generate_deck()
deck.shuffle_deck()

human = Human('Jason', 100)
comp = Computer()

bank = Bank()
bank.ask_bet(human)

hand = Hand(deck.cards)
hand.give_initial_cards(human, comp)
