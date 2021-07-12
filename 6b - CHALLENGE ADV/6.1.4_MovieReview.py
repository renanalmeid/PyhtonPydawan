# We want to create a function that will help us rate movies. 

#Our function will split the ratings into different ranges 
#and tell the user how the movie was based on the movie’s rating.

def movie_review(rating):
  if (rating <= 5):
    return "Avoid at all costs!"
  elif rating > 5 and rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."



###############
def movie_review(rating):
  if(rating <= 5):
    return "Avoid at all costs!"
  if(rating < 9):
    return "This one was fun."
  return "Outstanding!"
  