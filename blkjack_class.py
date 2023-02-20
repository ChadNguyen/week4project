class Blackjack:
    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.dealer = dealer
        self.player = player

    def deal_initial_cards(self):
        for i in range(2):
            self.player.hit(self.deck)
            self.dealer.hit(self.deck)

    def player_turn(self):
        while True:
            self.player.show_partial(self.dealer)
            choice = input('Do you want to hit, stand, or quit? ')
            if choice.lower() == 'hit':
                self.player.hit(self.deck)
                if self.player.is_busted():
                    print('You busted!')
                    return 'dealer'
            elif choice.lower() == 'stand':
                self.player.stand()
                return 'dealer'
            elif choice.lower() == 'quit':
                print('Thanks for playing!')
                exit()
        

    def dealer_turn(self):
        while self.dealer.must_hit():
            self.dealer.hit(self.deck)
            self.player.show_partial(self.dealer) 
        dealer_value = self.dealer.hand.get_value()
        if dealer_value > 21:
            print('Dealer busts! You win.')
            return 0
        else:
            return dealer_value

    def determine_winner(self, player_value, dealer_value):
        if player_value > 21:
            print('Player busts with', player_value, 'Dealer Wins.')
            return 'dealer'
        if dealer_value == player_value:
            print("It's a tie!")
            return 'tie'
        if dealer_value > 21:
            print('Dealer busts! Player wins with', player_value)
            return 'player'
        if dealer_value < player_value:
            print('Player wins with', player_value)
            return 'player'
        else:
            print('Dealer wins with', dealer_value)
            return 'dealer'

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



       
