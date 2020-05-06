class Hand:
    players = {}

    def __init__(self, cards, players):
        self.cards = cards

        for player in players:
            self.players[player.name] = {
                'shown cards': [],
                'hidden cards': []
            }

    def give_initial_cards(self, *args):
        for player in args:
            two_cards = self.cards[-2:]
            del self.cards[-2:]
            player.take_cards(two_cards)

    def show_current_game(self):
        for player in self.players:
            print(player)
