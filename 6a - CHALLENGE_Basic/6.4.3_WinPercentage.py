# we will create a function which calculates the percentage of games won

#n order to do this, we will need to know how many total games there were and divide the number of wins by the total number of games

# We also need to make sure that we return the result as a percentage

def win_percentage(wins, losses):
  total_game = wins+losses
  win_p = wins/total_game*100
  return win_p

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100