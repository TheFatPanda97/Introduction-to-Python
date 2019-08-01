import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
         'ten', 'jack', 'queen', 'king', 'ace']
values = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
          'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
          'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

playing = True


class Card:
    def __init__(self, suits, rank):
        self.suits = suits
        self.rank = rank

    def __str__(self):
        return self.rank + 'of' + self.suits


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_count = ''
        for card in self.deck:
            deck_count += '\n' + card.__str__()
        return 'The deck has' + deck_count

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value = values[card.rank]
        if card.rank == 'ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    while True:
        x = str(input(
            'would you like to hit or stand? Press h for hit and s for stand '))

        if x.lower() == 'h' or x.lower() == 'H':
            hit(deck, hand)
            return False
        elif x.lower() == 's' or x.lower() == 'S':
            print('player stands, it the dealers turn')
            return False
        else:
            print('please press either h or s: ')
            return True


def player_busts():
    print('player has busted!')
    chips.lose_bet()


def player_wins():
    print('the player has won!')
    chips.win_bet()


def dealer_busts():
    print('the player has won!')
    chips.win_bet()


def dealer_wins():
    print('the dealer has won!')
    chips.lose_bet()


def push():
    print("the player and the dealer has tied! It's a push!")


Player_total = 0
Dealer_total = 0
if True:
    print('welcome to blackjack')
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    Player_total += player_hand.value
    print('your first card is ' + str(player_hand.value))
    player_hand.add_card(deck.deal())
    Player_total += player_hand.value
    print('your second card is ' + str(player_hand.value))

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    Dealer_total += dealer_hand.value
    print('the dealers first card is ' + str(dealer_hand.value))
    dealer_hand.add_card(deck.deal())
    Dealer_total += dealer_hand.value
    print('the dealers second card is hidden')

    while True:
        if Player_total >= 21:
            break
        ask = str(input('do you want to hit? '))
        if ask == 'no' or ask == 'n':
            player_hand = Hand()
            break
        elif ask == 'yes' or ask == 'y':
            player_hand = Hand()
            player_hand.add_card(deck.deal())
            Player_total += player_hand.value
            print('your next card is ' + str(player_hand.value))
            print('player total is ' + str(Player_total))
        else:
            print('please input yes or no ')
            continue

    while True:
        if Dealer_total >= 17:
            break
        elif Dealer_total < 17:
            dealer_hand.add_card(deck.deal())
            Dealer_total += dealer_hand.value
            print('dealers next card is ' + str(dealer_hand.value))
            continue
        else:
            break
    print('dealer total is ' + str(Dealer_total))

    while True:
        if Player_total > 21:
            if Dealer_total > 21:
                print('the dealer has won')
            else:
                print('the player has busted')
            break
        elif Player_total == 21:
            if Dealer_total == 21:
                print('the dealer has won')
            else:
                print('the player has won')
            break
        elif Player_total < 21:
            if Dealer_total >= Player_total and Dealer_total <= 21:
                print('the dealer has won')
            else:
                print('the player has won')
            break
