from exceptions import NotEnoughtFunds


class Bank():
    def __init__(self, bank=0):
        self.bank = bank
        self.bets = {}

    def ask_bet(self, player):
        try:
            # TODO: make a validation for player (that it is a class)
            player_name = player.name
            bet_value = int(input(f'Please, make your bet, {player_name}: '))
            player.make_bet(bet_value)
            isEnoughMoney = self.check_player_funds(player, bet_value)

            if not isEnoughMoney:
                raise NotEnoughtFunds('Not enought money in a player bank.',
                                      'Sorry, you don\'t have enought money. Please, try to low your bet.')

            self.bets[player_name] = bet_value
        except NotEnoughtFunds:
            self.ask_bet(player)

    def check_player_funds(self, player, bet):
        return player.bank >= bet
