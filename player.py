class Player:

    def hit(self):
        pass

    def stand(self):
        pass

    def make_bet(self, amount):
        self.bank = self.bank - int(amount)
        return amount

    def take_cards(self, cards):
        for card in cards:
            self.cards[card.name] = card

    def examine_your_cards(self):
        pass

    def show_cards(self, cards):
        return f'{self.name}, open cards: {cards}'
