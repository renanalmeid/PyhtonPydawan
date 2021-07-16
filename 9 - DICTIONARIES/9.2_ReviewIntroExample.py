#We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the amount of times each song has been played.

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

#Using a list comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount pair for each song in songs and each playcount in playcounts.

plays = {key:value for key, value in zip(songs, playcounts)}

print(plays)
#After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1.
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})

library = {"The Best Songs": plays, "Sunday Feelings": {}}


print(library)