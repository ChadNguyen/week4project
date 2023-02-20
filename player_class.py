import random
from card_deck_class import Hand
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def hit(self, deck):
        self.hand.add_card(deck.draw_card())
        print("Player's Hand:")
        for card in self.hand.cards:
            print(card)
        print("Player's Hand Value:", self.hand.get_value())

    def stand(self):
        print(f"{self.name} stands.")
        return 'dealer'

    def is_busted(self):
        return self.hand.get_value() > 21

    def show_partial(self, dealer):
        print("\nDealer's Hand: ")
        print(" <card hidden>")
        print(dealer.hand.cards[1])
        print("Dealer's Hand Value:", dealer.hand.cards[1].value)
        print("\nPlayer's Hand:")
        for card in self.hand.cards:
            print(card)
        print("Player's Hand Value:", self.hand.get_value())

    def show_all(self, dealer):
        print("\nDealer's Hand:")
        for card in dealer.hand.cards:
            print(card)
        print("Dealer's Hand Value:", dealer.hand.get_value())
        print("\nPlayer's Hand:")
        for card in self.hand.cards:
            print(card)
        print("Player's Hand Value:", self.hand.get_value())
    
    def check_hand(self):
        value = 0
        has_ace = False
        for card in self.hand.cards:
            if card.value == 1:
                has_ace = True
            value += min(card.value, 10)
        if has_ace and value + 10 <= 21:
            value += 10
        return value


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def hit(self, deck):
        self.hand.add_card(deck.draw_card())

    def must_hit(self):
        """Dealer must hit on Soft 17."""
        if self.hand.get_value() < 17:
            return True
        elif self.hand.get_value() == 17:
            for card in self.hand.cards:
                if card.rank == "Ace":
                    return True
            return False
        elif self.hand.get_value() > 21:
            return False

    def show_partial(self, dealer):
        print("\nDealer's Hand: ")
        print(" <card hidden>")
        print(dealer.hand.cards[1])
        print("Dealer's Hand Value:", dealer.hand.cards[1].value)
        for card in self.hand.cards:
            print(card)
        print("Player's Hand Value:", self.hand.get_value())

    def show_all(self, dealer):
        print("\nDealer's Hand:")
        for card in dealer.hand.cards:
            print(card)
        print("Dealer's Hand Value:", dealer.hand.get_value())
        print("\nPlayer's Hand:")
        for card in self.hand.cards:
            print(card)
        print("Player's Hand Value:", self.hand.get_value())
    
    def check_hand(self):
        value = 0
        has_ace = False
        for card in self.hand.cards:
            if card.value == 1:
                has_ace = True
            value += min(card.value, 10)
        if has_ace and value + 10 <= 21:
            value += 10
        return value


