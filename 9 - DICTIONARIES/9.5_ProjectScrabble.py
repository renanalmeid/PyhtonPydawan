#In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#We would like to combine these two into a dictionary that would map a letter to its point value.
letter_to_points = {key:value for key, value in zip(letters, points)}
#Our letters list did not take into account blank tiles. Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points.update({" ": 0})

#We want to create a function that will take in a word and return how many points that word is worth.
def score_word(word):
  point_total = 0

#After defining point_total, create a for loop that goes through the letters in word and adds the point value of each letter to point_total.
#You should get the point value from the letter_to_points dictionary. If the letter you are checking for is not in letter_to_points, add 0 to the point_total.

  for letter in word:
    point_total += letter_to_points.get(letter, 0)

  return point_total

brownie_points = score_word("BROWNIE")

#print(brownie_points)


############Score a Game
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],   "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points ={}

for player,words in player_to_words.items():
  player_points=0
#Iterate through the items in player_to_words. Call each player player and each list of words words.Within your loop, create a variable called player_points and set it to 0.
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

#After the inner loop ends, set the current player value to be a key of player_to_points, with a value of player_points.

#player_to_points should now contain the mapping of players to how many points they’ve scored. Print this out to see the current standings for this game!
print(player_to_points)



























