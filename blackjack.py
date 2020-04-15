import random
suits=('hearts','diamonds','spades','clubs')
ranks=('two','three','four','five','six','seven','eight','nine','jack','queen','king','ace')
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'jack':10,'queen':10,'king':10,'ace':11}
playing=True
class Card():
    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks
    def __str__(self):
        return self.ranks + ' \tof\t' +self.suits
class Deck():
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp +='\n' + card.__str__()
        return 'the deck has :'+ deck_comp
    def shuff(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card    

class Hand():
    def __init__(self):
        self.cards=[]
        self.values=0
        self.ace=0
    def add_card(self,card):
        self.cards.append(card)
        self.values += values[card.ranks]
        if card.ranks=='ace':
            self.ace +=1
    def adjust_ace(self):
        while self.values>21 and self.ace:
            self.values -=10
            self.ace -=1

            

class Chips():
    def __init__(self,total=100,bet=50):
        self.total=total
        self.bet=bet
    def win_bet(self):
        self.total += self.bet    
    def lose_bet(self):
        self.total -= self.bet
    
def bet(chips):
    while True :
      try:
        chips.bet=int(input('enter your bet:'))
      except:
        print("wromng entry")
      else:
         if chips.bet>chips.total:
             continue
         else:
            break     
def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_ace()
def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x=input('enter hit or stand')
        if x[0].lower()=='h':
           hit(deck,player_hand)
        elif x[0].lower()=='s':
            print('player stands dealers turn')
            playing=False    
        else :
            print('wrong entry')
            continue   
        break   
def player_busts(player,dealer,chips):
    print('player busted')
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print('player wins')
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print('dealer busted')
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print('dealer wins')
    chips.lose_bet()                    
def push(player,dealer,chips):
    print('player dealer tie push')
def show_some(player,dealer):
    print('dealer hand:')
    print(dealer.cards[1])
    print('player hand')
    for i in player.cards:
        print('\n')
        print(i)
def show_all(player,dealer):
    print('dealer hand:')
    for n  in dealer.cards:
        print('\n')
        print(n)        
    print('player hand')
    for x in player.cards:
        print('\n')
        print(x)

while True:
    print('welcome to blackjack')
    deck=Deck()
    deck.shuff()
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    player_chips=Chips()

    bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.values>21:
          player_busts(player_hand,dealer_hand,player_chips)
          break
    if player_hand.values<=21:

        while dealer_hand.values<player_hand.values:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand) 
        if dealer_hand.values>21:
                dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.values>player_hand.values:
                dealer_wins(player_hand,dealer_hand,player_chips)
        elif player_hand.values>dealer_hand.values:
                player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand,player_chips)
    print('\n')
    print(f'player chips:{player_chips.total}')
    j=input('to play again type y or vice versa:')
    if j=='y':
        playing=True
        continue            
    else:
        break





         
   


           