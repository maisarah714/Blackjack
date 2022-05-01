############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def ace_card(cards):
  if sum(cards) >21 and 11 in cards:
    cards[cards.index(11)] = 1

play = 'y'

while play == 'y':
  print(logo)
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n").lower()

  clear()
  
  card_1 = random.choices(cards, k=2)
  card_2 = random.choices(cards, k=2)
  
  add_card = 'y'
  while add_card == 'y':
    print(f"Your cards: {card_1}, current score: {sum(card_1)}")
    print(f"Computer's first card: {card_2[0]}")
  
    if sum(card_2) == 21:
      print("Opponent got Blackjack! You lose!")
      add_card = 'n'
      continue
    elif sum(card_1) == 21 and sum(card_2) == 21:
      print("It's a draw!")
      add_card = 'n'
      continue
    elif sum(card_1) == 21:
      print("You got Blackjack! You won!")
      add_card = 'n'
      continue

    if sum(card_1) >21 or sum(card_2) >21:
      add_card = 'n'
      continue
      
    add_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if add_card =='y':
      card_1 += random.choices(cards)
      ace_card(card_1)
      continue
  
    
    while sum(card_2) <= 16:
      card_2 += random.choices(cards)
      ace_card(card_2)
    
    
  print(f"Your final hand: {card_1}, current score: {sum(card_1)}")
  print(f"Computer's final hand: {card_2}, final score: {sum(card_2)}")
  
  
  if sum(card_1) >21:
      print("You went over. You lose 😭")
  elif sum(card_2) >21:
      print("Opponent went over. You won 😁")
  elif sum(card_1) > sum(card_2):
    print("You won 😁")
  elif sum(card_1) < sum(card_2):
    print("You lose 😤")
  else:
    print("Draw!")
