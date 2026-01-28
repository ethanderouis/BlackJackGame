# BLACKJACK
card_values = {
  "A": [1, 11], 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10
}

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
    
#player_name = input("What is your name:") -- put these as arguments to make the class
#current_money = input("How much money can you lose tonight:") -- put these as arguments to make the class

gambler = Player("Ethan", 100)

gambler.bet(100)
gambler.win()
print(gambler) # at 200 

gambler.bet(50)
gambler.win()
print(gambler) # at 250

gambler.bet(50)
gambler.lose()
print(gambler) # at 200