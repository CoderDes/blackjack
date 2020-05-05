class Player:

    def hit(self):
        pass

    def stand(self):
        pass

    def make_bet(self, amount):
        self.bank = self.bank - int(amount)
        return amount

    def take_cards(self, *args):
        self.cards = self.cards + list(args)
