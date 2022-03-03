
#########################  Card and Deck Class ###########################


import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three','Four', 'Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

playing = True



class Card():
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        
        return self.rank + " of " + self.suit
        


class Deck():
    
    def __init__(self):
        
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: "+ deck_comp
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
            


test_deck = Deck()
test_deck.shuffle()
print(test_deck)



#############################. Hand and Chip class!!!!##########################



class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        #card passed in
        #from Deck.deal() --> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
        
        #track our aces here
        if card.rank == 'Ace':
            self.aces += 1
        
    def adjust_for_ace(self):
        
        # if total value > 21 and i still have an ace
        #then change my ace to a 1 instead of an 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1



test_deck = Deck()
test_deck.shuffle()

# player
test_player = Hand()
pulled_card = test_deck.deal()
test_player.add_card
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)


################################ CHIPES CLASS ######################



class Chips():
    
    def __init__(self,total=100): #make up number for bet by using 100
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet



##############################  FUNCTIONS FOR GAME PLAY #####################################


def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please provide an integer.")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips. You have {}".format(chips.total))
            else:
                break
                



def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()



def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input('Hit or Stand? Enter h or s')
        
        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        
        else:
            print("Sorry I didn't understand that, please enter an h or s only!")
            continue
        break



def show_some(player,dealer):
    
    # Show only ONE of the dealer's cards
    print(' ')
    print("DEALER'S HAND: ")
    print('First card hidden!')
    print(dealer.cards[1])
    
    # Show all (2 cards) of the player's hand/cards
    print(' ')
    print("PLAYER'S HAND:")
    for card in player.cards:
        print(card)
    
    
    
def show_all(player,dealer):
    
    # show all the dealer's cards
    print(' ')
    print("DEALER'S HAND:")
    for card in dealer.cards:
        print(card)
    
    #calculate and display value 
    print(' ')
    print(f"Value of Dealer's hand is: {dealer.value}")
    
    #show all the players cards
    print(' ')
    print("PLAYER'S HAND:")
    for card in player.cards:
        print(card)
    print(' ')
    print(f"Value of Player's hand is: {player.value}")




def player_busts(player,dealer,chips):
    print("BUST!")
    chips.lose_bet()
    
def player_wins(player,dealer,chips):
    print("Player WINS!")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print('Player WINS! Dealer BUSTED!')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer WINS!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and player tie! PUSH")



######################################  GAME PLAY ########################################



while True:
    
    print("WELCOME TO BLACKJACK!")
    
    #create and shuffle deck
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    #set up players chips
    player_chips = Chips()
    
    #prompt player for their bet
    take_bet(player_chips)
    
    #show cards (but keep dealers secret)
    show_some(player_hand,dealer_hand)
    
    while playing:  #recall this variable from our hit_or_stand function
        
        #prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        #show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        #if player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            
            break
            
            
    #if player hasn't busted, play dealers hand until dealer gets to 17
    if player_hand.value <= 21:
            
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
                
        #show all cards
        show_all(player_hand,dealer_hand)
            
        #run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
                
    #inform player of their chips total
    print('Player total chips are at: {}'.format(player_chips.total))
        
    #ask to play again
    new_game = input('Would you like to play another hand? y/n')
        
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing')
        
        break
    





