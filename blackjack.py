import random
import os
# python clear concole function cls()
def cls():
  os.system('cls' if os.name=='nt' else 'clear')

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""



def deal():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if len(cards) == 2 and sum(cards) == 21:
    # we are returning 0 in case of a blackjack the if statement above checks if we hav
    # two cards which sum would be 21 if there are 10 , 11 cards are present in deck
    return 0
  if len(cards) == 2 and sum(cards) > 21:
    # we cannot use replace method because it only works with strings not int
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(player_score, bot_score):
  # Condition 1: If both user and computer are over 21, the user loses automatically.
  if player_score > 21 and bot_score > 21:
      return "!!! You went over. You lose !!!\n"

  # Condition 2: Check for a draw
  if player_score == bot_score:
      return "!!! Draw !!!\n"

  # Condition 3: If the computer has Blackjack (score = 0), the user loses.
  elif bot_score == 0:
      return "!!! Lose, opponent has Blackjack !!!\n"

  # Condition 4: If the user has Blackjack (score = 0), the user wins.
  elif player_score == 0:
      return "!!! Win with a Blackjack !!!\n"

  # Condition 5: If the user's score is over 21, the user loses.
  elif player_score > 21:
      return "!!! You went over. You lose !!!\n"

  # Condition 6: If the computer's score is over 21, the computer loses.
  elif bot_score > 21:
      return "!!! Opponent went over. You win !!!\n"

  # Condition 7: If none of the above, compare scores; the highest score wins.
  elif player_score > bot_score:
      return "!!! You win !!!\n"
  else:
      return "!!! You lose !!!\n"


def blackjack():
  
  print(logo)
  player = []
  bot = []
  game_over = False
  
  for _ in range(2):
    player_new = deal()
    player.append(player_new)
    bot_new = deal()
    bot.append(bot_new)
  
  
  
  while game_over is False:
    player_score = calculate_score(player)
    bot_score = calculate_score(bot)
    
    print(f"Your cards: {player}, current score: {player_score}\n")
    print(f"Computer's first card: {bot[0]}\n")
  
    if player_score == 0 or bot_score == 0 or player_score > 21:
      game_over = True
    else:
      draw = input("Press 'y' to draw another card: \n")
      if draw == "y":
        player_new = deal()
        player.append(player_new)
      else:
        game_over = True
  
  while bot_score != 0 and bot_score < 17:
    bot_new = deal()
    bot.append(bot_new)
    bot_score = calculate_score(bot)
  
  result = compare(player_score,bot_score)
  print(result)
  print(f"Your final hand: {player}, final score: {player_score}\n")
  print(f"Computer's final hand: {bot}, final score: {bot_score}\n")


print(logo)
while input("!!! Press 'y' to try your luck in BLACKJACK !!!") == "y":
  cls()
  blackjack()
