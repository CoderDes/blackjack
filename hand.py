class Hand:
    points = {}
    max_value = 21
    max_dealer_points = 17

    def __init__(self, cards, players):
        # TODO: make a validation for players argument. Must be a list
        self.cards = cards
        self.players = players

        for player in players:
            if player.name.lower != 'dealer':
                self.current_player = player
                break

    def give_initial_cards(self, *args):
        for player in args:
            two_cards = self.cards[-2:]
            del self.cards[-2:]
            player.take_cards(two_cards)

    def show_current_game(self):
        print(self.points)

    def ask_player(self, player):
        if (self.current_player.name.lower() == 'dealer') and (self.points[self.current_player.name] >= self.max_dealer_points):
            self.calc_players_points()
            self.win_lose()
            return

        answer = input('Hit or take a card: ')

        if answer.lower() == 'hit':
            self.current_player.hit(self.cards.pop())
        else:
            self.current_player.stand()
            self.switch_player()

        self.calc_players_points()
        self.show_current_game()

        if not self.check_busted_players():
            self.ask_player(self.current_player)
        else:
            self.win_lose()

    def switch_player(self):
        current_player_index = self.players.index(self.current_player)
        next_player_index = current_player_index + 1

        if next_player_index == len(self.players):
            next_player_index = 0

        self.current_player = self.players[next_player_index]
        print('Current player is', self.current_player.name)

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

    def win_lose(self):
        max_player = max(self.points, key=self.points.get)

        if self.points[max_player] < 21:
            print(f'{max_player} wins!')
        else:
            print(f'{max_player} lose!')
