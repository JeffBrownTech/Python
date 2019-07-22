# Codecademy 'Learn Python 3' Scrabble Project
# Create Scrabble score keeper that keeps track of words played and a player's total score
# This script incorporates the 'Ideas for Further Practice!' section of the project such as
#  1. Add play_word() function that takes a player and word to add to list of words the player has played
#  2. Add update_point_totals() function that updates players' total scores when called
#  3. Update letter_to_points dictionary to handle lowercase input as well

#----------------------------------------------------------------------------

# Ideas for additional improvements
# -Combine playing a word, scoring the word, and adding to the player's overall score in one step
# -Ability to add player's to player_to_words from a blank dictionary before starting the game

#----------------------------------------------------------------------------

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create a dictionary using list comprehension and zip
letter_to_points = {key:value for key, value in zip(letters,points)}

# Add lower case letterse to dictionary
all_letter_to_points = {}
for key, value in letter_to_points.items():
    all_letter_to_points[key] = value
    all_letter_to_points[key.lower()] = value

# Add value for blank tiles
all_letter_to_points[" "] = 0

# Create a function that takes in a word and calculates the point total for the word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += all_letter_to_points.get(letter, 0)
  return point_total

# Create a function to take in a player and a word to add to the existing dictionary
def play_word(player, word):
    player_to_words.get(player).append(word)

# Create dictionary with players and words they have played
player_to_words = {'player1': [], 'wordNerd': [], 'Lexi Con': [], 'Prof Reader': []}

# Create dictionary to hold player's points/total score
player_to_points = {}

# Create a function to update the player's point totals after a word is played
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points

# Populate player's played words
play_word('player1', 'blue')
play_word('player1', 'TENNIS')
play_word('player1', 'EXiT')

play_word('wordNerd', 'earth')
play_word('wordNerd', 'EYES')
play_word('wordNerd', 'MacHInE')

play_word('Lexi Con', 'ERASER')
play_word('Lexi Con', 'beLly')
play_word('Lexi Con', 'husky')

play_word('Prof Reader', 'zap')
play_word('Prof Reader', 'coma')
play_word('Prof Reader', 'period')

# Update player's totals and print word list and score
update_point_totals()
print(player_to_words)
print(player_to_points)

# Add more words
play_word('player1', 'butter')
play_word('wordNerd', 'WomBat')
play_word('Lexi Con', 'tiger')
play_word('Prof Reader', 'dentist')

# Update player's totals and print word list and score
update_point_totals()
print(player_to_words)
print(player_to_points)