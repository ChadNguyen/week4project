from card_deck_class import Card, Deck, Hand
from player_class import Player, Dealer
from blkjack_class import Blackjack
import random

def play(self):
    self.deck.shuffle()
    self.deal_initial_cards()
    while True:
        dealer_value = int(self.dealer.hand.get_value())
        player_value = int(self.player.hand.get_value())
        if player_value == 21:
            print('Blackjack! You win.')
            break
        action = self.player_turn()
        if action == 'stand':
            print("Player stands.")
            return 'dealer'
        elif action == 'dealer':
            dealer_value = self.dealer_turn()
        if self.player.is_busted():
            self.determine_winner(self.player.hand.get_value(), self.dealer.hand.get_value())
            break
        if dealer_value == player_value:
            self.player.show_all(self.dealer)
            self.determine_winner(player_value, dealer_value)
            break
        if dealer_value > 21:
            print('Dealer busts! Player wins with', player_value)
        elif player_value > dealer_value:
            print('Player wins with', player_value)
        elif dealer_value > player_value:
            print('Dealer wins with', dealer_value)
        else:
            print("It's a tie! Both player and dealer have a hand value of", player_value)
            
deck = Deck()
player = Player("Player")
dealer = Dealer()
game = Blackjack(deck, player, dealer)
game.play()

