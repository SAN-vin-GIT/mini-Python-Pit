import random
import os
# python clear concole function cls()
def cls():
  os.system('cls' if os.name=='nt' else 'clear')
word_list = [
    "abacus",
    "battalion",
    "carnivorous",
    "dichotomy",
    "ephemeral",
    "fortitude",
    "gargoyle",
    "harbinger",
    "ichthyology",
    "juxtaposition",
    "kaleidoscope",
    "labyrinthine",
    "misanthrope",
    "nebulous",
    "oligarchy",
    "palindrome",
    "quintessential",
    "rejuvenate",
    "serendipity",
    "transcend",
    "ubiquitous",
    "vicarious",
    "wavelength",
    "xenophobia",
    "yesteryear",
    "zephyr",
    "alchemy",
    "beguile",
    "cacophony",
    "dystopia",
    "effervescent",
    "fathomless",
    "gossamer",
    "hyperbole",
    "insidious",
    "juxtapose",
    "kismet",
    "languid",
    "metamorphosis",
    "nostalgia",
    "obfuscate",
    "panacea",
    "quagmire",
    "rendezvous",
    "susurrus",
    "tapestry",
    "ubiquity",
    "veneration",
    "whimsical",
    "xylophone",
    "yearning",
    "zenith",
    "antithesis",
    "brouhaha",
    "cognizant",
    "doppelgänger",
    "efficacious",
    "felicity",
    "grandiloquent",
    "harangue",
    "ineffable",
    "juxtaposition",
    "kaleidoscopic",
    "lascivious",
    "magnanimous",
    "nefarious",
    "obsequious",
    "paradigm",
    "quintessence",
    "recalcitrant",
    "sonder",
    "terse",
    "unfathomable",
    "voracious",
    "winsome",
    "xenon",
    "yoke",
    "zenithal",
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
]

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ 
                   
                   '''

word = random.choice(word_list)
lives = 6
# this is for debuging :: print("Chosen word:", word)
print(logo)
print("Here is your Word!!! \n")

# assigning an null value to dashed which will add amount of strings in a chosen word and print dashes correspondingly
dashed = []
for items in word:
  dashed += "_"
print(dashed)

# declaring a game_over boolean to control game state
game_over = False
while not game_over:

  if lives == 6:
    print(stages[5])
  elif lives == 5:
    print(stages[4])
  elif lives == 4:
    print(stages[3])
  elif lives == 3:
    print(stages[2])
  elif lives == 2:
    print(stages[1])
  elif lives == 1:
    print(stages[0])
    print("This is the last stage think carefully and")
    # print(stages[lives]) ::replace lines from 95 to 106 with this print statement ::

  guess = input("Guess a letter \n").lower()
  cls()
  if guess in dashed:
    print(f"Bro you've already guessed {guess}")

  # position accurires the length of the word and assigns to letter which is later checked by if statement to see if it is same as the guess and if   yes the postion of dash changes to the corresponding letter
  for position in range(len(word)):
    letter = word[position]
    if letter == guess:
      dashed[position] = letter

  if guess not in word:
    print(f"Well {guess} is not in the word, so you lose a life.")
    lives -= 1

# joining all elements and turning into a string
  print(f"{' '.join(dashed)}")

  # when the conditons of game_over are met it switched to false breaking while loop and printing gameover message

  if "_" not in dashed:
    game_over = True
    print("You Won!")
  elif lives <= 0:
    game_over = True
    print("You Lose!\n")
    print(f"The Word Was: {word}")
