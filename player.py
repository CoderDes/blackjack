class Player:

    def hit(self, card):
        print(f'{self.name} hits! {card.name}')
        self.cards[card.name] = card

    def stand(self):
        pass

    def make_bet(self, amount):
        self.bank = self.bank - int(amount)
        return amount

    def take_cards(self, cards):
        for card in cards:
            if 'ace' in card.name:
                card.card_value = card.ace_define()
            self.cards[card.name] = card

    def examine_your_cards(self):
        print(self.cards)

    def show_cards(self, cards):
        return f'{self.name}, open cards: {cards}'
