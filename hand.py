class Hand:
    points = {}
    max_value = 21

    def __init__(self, cards, players):
        # TODO: make a validation for players argument. Must be a list
        self.cards = cards
        self.players = players

    def give_initial_cards(self, *args):
        for player in args:
            two_cards = self.cards[-2:]
            del self.cards[-2:]
            player.take_cards(two_cards)

    def show_current_game(self):
        print(self.points)

    def ask_player(self, player):
        answer = input('Hit or take a card: ')

        # TODO: make a validation for answer and recursion
        if answer.lower() == 'hit':
            player.hit(self.cards.pop())
        else:
            player.stand()

        self.calc_players_points()
        self.show_current_game()

        if not self.check_busted_players():
            self.ask_player()

    def calc_players_points(self):

        for player in self.players:
            player_name = player.name
            player_points = 0

            for card in player.cards.values():
                player_points = player_points + card.card_value

            self.points[player_name] = player_points

    def check_busted_players(self):
        def filter_players(arg):
            player, point = arg

            if point >= 21:
                return player

        busted_players = list(
            filter(filter_players, self.points.items()))

        return len(busted_players)
