######### Reading files

#with open('real_cool_document.txt') as cool_doc:
#  cool_contents = cool_doc.read()
#print(cool_contents)

with open('welcome.txt') as text_file:
  text_data = text_file.read()

print(text_data)


##############Iterating Through Lines

#When we read a file, we might want to grab the whole document in a single string, like .read() would return.
#But what if we wanted to store each line in a variable? We can use the .readlines() function to read a text file line by line instead of having the whole thing.


#Using a with statement, create a file object pointing to the file how_many_lines.txt. Store that file object in the variable lines_doc.
with open('how_many_lines.txt') as lines_doc:

#Iterate through each of the lines in lines_doc.readlines() using a for loop.Inside the for loop print out each line of how_many_lines.txt.
  for lines in lines_doc.readlines():
    print(lines)


########## Reading a Line

#Sometimes you don’t want to iterate through a whole file. For that, there’s a different file method, .readline(), which will only read a single line at a time. If the entire document is read line by line in this way subsequent calls to .readline() will not throw an error but will start returning an empty string ("").

with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  a = first_line_doc.readline()
print(first_line)
print(a)


########## Writing a file 
#Reading a file is all well and good, but what if we want to create a file of our own? 
#It turns out that our open() function that we’re using to open a file to read needs another argument to open a file to write to.

#with open('generated_file.txt', 'w') as gen_file:
#  gen_file.write("What an incredible file!")

#Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode. The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.

#This code creates a new file in the same folder as script.py and gives it the text What an incredible file!. It’s important to note that if there is already a file called generated_file.txt it will completely overwrite that file, erasing whatever its contents were before.

with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write("Isa bartani")


########### Appending to a File
#Isn’t there a way to just add a line to a file without completely deleting it?

#Of course there is! Instead of opening the file using the argument 'w' for write-mode, we open it with 'a' for append-mode. If we have a generated file with the following contents:


with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write("Air Buddy")

  ################ WHATS WITH "with"??

#The with keyword invokes something called a context manager for the file that we’re calling open() on. 

#This context manager takes care of opening the file when we call open() and then closing the file after we leave the indented block.

#The with syntax replaces older ways to access files where you need to call .close() on the file object manually. We can still open up a file and append to it with the old syntax, as long as we remember to close the file connection afterwards.


with open('fun_file.txt') as close_this_file: 

  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)
