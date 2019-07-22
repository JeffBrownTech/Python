# Codecademy 'Learn Python 3' Scrabble Project
# Create Scrabble score keeper that keeps track of words played and a player's total score

#----------------------------------------------------------------------------

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create a dictionary using list comprehension and zip
letter_to_points = {key:value for key, value in zip(letters,points)}

# Add value for blank tiles
letter_to_points[" "] = 0

# Create a function that takes in a word and calculates the point total for the word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

# Test the function using BROWNIE
brownie_points = score_word("BROWNIE")
print(brownie_points) # Should return 15

# Create dictionary with players and words they have played
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

# Iterate through each player and played words to calculate the score and add to a new dictionary
player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)