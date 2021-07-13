highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#Step1
print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(',')
print("-----------------------")

#Step 2
print(highlighted_poems_list)
print("-----------------------")

#Step 4-5
highlighted_poems_stripped =[]
for index in highlighted_poems_list:
  highlighted_poems_stripped.append(index.strip())

print(highlighted_poems_stripped)
print("-----------------------")

#Step 6-7
highlighted_poems_details =[]
for index2 in highlighted_poems_stripped:
  highlighted_poems_details.append(index2.split(':'))

#Step 8
titles =[]
poets = []
dates = []

#Step 9
for index3 in highlighted_poems_details:
  titles.append(index3[0])
  poets.append(index3[1])
  dates.append(index3[2])

#Step 10 
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))

    