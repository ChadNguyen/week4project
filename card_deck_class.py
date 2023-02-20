import random

class Card:
    CARD_SUITS = ['♠', '♣', '♥', '♦']
    CARD_RANKS = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.CARD_RANKS[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.CARD_SUITS:
            for rank in Card.CARD_RANKS:
                self.deck.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self): # shuffle deck in random order
        random.shuffle(self.deck)

    def draw_card(self): #pick out cards from the deck for game round.
        single_card = random.choice(self.deck)
        self.deck.remove(single_card)
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # can be 1 or 11

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace':
            self.aces += 1
        self.ace_cards()

    def ace_cards(self):
        while self.value > 21 and self.aces:
            if self.value - 10 <= 21:
                self.value -= 10
                self.aces -= 1
            else:
                break

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.rank == 'Ace':
                num_aces += 1
                value += 11
            elif card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            else:
                value += card.value
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value



