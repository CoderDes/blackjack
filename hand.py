class Hand:
    def __init__(self, cards):
        self.cards = cards

    def give_initial_cards(self, *args):
        for player in args:
            two_cards = self.cards[-2:]
            player.take_cards(two_cards)
