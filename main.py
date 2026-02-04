# imports
import random

# BLACKJACK
# creating a deck of cards
def create_deck():
    cards = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10
    }

    deck = []
    for card, value in cards.items():
        deck.extend([(card, value)] * 4)  # 4 of each card

    random.shuffle(deck)
    return deck

class Player:
  def __init__(self, name, money, current_bet=0):
    self.name = name
    self.money = money
    self.current_bet = current_bet

  def __repr__(self):
    return "{name} has {money} to lose or multiply tonight folks and he is currently betting {current_bet}.".format(name=self.name, money=self.money, current_bet = self.current_bet)

  def bet(self, value):
    if value <= self.money:
      self.money -= value
      self.current_bet = value
      print("{name} just placed a bet for {value} and you currently have {money_minus_current_bet}".format(name=self.name, value=value, money_minus_current_bet=self.money))
    else:
      print("You do not have sufficient funds")

  #def card_values(self):

  def win(self):
    print("You won! You get {current_bet}".format(current_bet = self.current_bet*2))
    self.money += (self.current_bet*2)
    self.current_bet = 0

  def lose(self):
    print("House wins")
    print("You lost {current_bet} and currently have {money}".format(current_bet = self.current_bet, money = self.money))
    self.current_bet = 0


class Dealer:
  def __init__(self, card_list=[]):
    self.card_list = card_list

  def __repr__(self):
    return "Dealer's current hand {dealer_hand}".format(dealer_hand=self.card_list)
  
  def starting_card(self, current_card_deck):
    self.card_list.append(current_card_deck.pop())
    print(self.card_list)

class Hand:
  def __init__(self, card_list=[]):
    self.card_list = card_list

  def __repr__(self):
    return str(self.card_list)
  
  def starting_cards(self, current_card_deck):
    self.card_list.append(current_card_deck.pop())
    self.card_list.append(current_card_deck.pop())
    print(self.card_list)


  
  def hit_pass_bust(self, card_value):    
    self.card_list.append(card_value) # will be appending the card here
    
    total = sum(self.card_list)
    if total < 21:
      print("can still hit")
    elif total == 21:
      print("stay, you are at 21")
    else:
      print("over 21 bust")


print("Welcome to Terminal BlackJack - where we act like we have money and still lose it anyways.")
#player_name = input("What is your name? ")
#current_money = input("How much money did you bring today? ")
player_name = "Ethan"
current_money = int("1000")
gambler = Player(player_name, current_money)
print(gambler)



def play(gambler):
  # player bets how much they want for the round
  round_bet = int("500") #int(input("What will you be betting this round? "))
  gambler.bet(round_bet)

  # dealer deals 2 cards for the players and 1 for dealer
  current_deck = create_deck()
  print(current_deck)

  player_hand = Hand()
  print("CARD LIST FOR PLAYER HERE")
  player_hand.starting_cards(current_deck)

  dealer_hand = Dealer()
  dealer_hand.starting_card(current_deck)

  # players ask to hit or stay - this step can end the round
  # dealer hits until his cards sum is >= 17 value -- if playeer does not bust, this tells player if he wins or not


while True:
  play(gambler)

  play_again = input("Would you like to play again(y/n)?")

  if play_again.lower() != "y":
    print("Thanks for playing")
    break
  















# make it more advance:
# ace needs to have two values
# visuals will allow to add some suits