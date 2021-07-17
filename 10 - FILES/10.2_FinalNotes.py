############What Is a CSV File?

#CSV files are an example of a text file that impose a structure to their data. CSV stands for Comma-Separated Values and CSV files are usually the way that data from spreadsheet software (like Microsoft Excel or Google Sheets) is exported into a portable format.

#Notice that the first row of the CSV file doesn’t actually represent any data, just the labels of the data that’s present in the rest of the file. The rest of the rows of the file are the same as the rows in the spreadsheet software, just instead of being separated into different cells they’re separated by… well I suppose it’s fair to say they’re separated by commas.

with open('logger.csv') as log_csv_file:
  what = log_csv_file.read()

print(what)

############Reading a CSV File
# there are ways to access the data in a format better suited for programming purposes
#n Python we can convert that data into a dictionary using the csv library’s DictReader object. 


#We pass the additional keyword argument newline='' to the file opening open() function so that we don’t accidentally mistake a line break in one of our data fields as a new row in our CSV

#After opening our new CSV file we use csv.DictReader(users_csv) which converts the lines of our CSV file to Python dictionaries which we can use access methods fo
# The keys of the dictionary are, by default, the entries in the first line of our CSV file. Since our CSV’s first line calls the third field in our CSV “Email“, we can use that as the key in each row of our DictReader.
#When we iterate through the rows of our user_reader object, we access all of the rows in our CSV as dictionaries (except for the first row, which we used to label the keys of our dictionary). By accessing the 'Email' key of each of these rows we can grab the email address in that row and append it to our list_of_email_addresses.

import csv 

with open('cool_csv.csv', newline='') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])


########Reading Different Types of CSV Files
# but it’s also true that other ways of separating values are valid CSV files these days.

#So we call all files with a list of different values a CSV file and then use different delimiters (like a comma or tab) to indicate where the different values start and stop.

#usar um argumehto secundario no .DictReader para que delimite-se o separador de informações

import csv
with open('books.csv') as books_csv:

#Create a DictReader instance that uses the @ symbol as a delimiter to read books_csv. Save the result in a variable called books_reader.

  books_reader =csv.DictReader(books_csv, delimiter='@')
#Create a list called isbn_list, iterate through books_reader to get the ISBN number of every book in the CSV file. Use the ['ISBN'] key for the dictionary objects passed to it.
  isbn_list = [book['ISBN'] for book in books_reader]

#############Writing a CSV File

#1) We import the csv library, and then open a new CSV file in write-mode by passing the 'w' argument to the open() function.

#2)We then define the fields we’re going to be using into a variable called fields. We then instantiate our CSV writer object and pass two arguments. The first is output_csv, the file handler object. The second is our list of fields fields which we pass to the keyword parameter fieldnames.

#3)Now that we’ve instantiated our CSV file writer, we can start adding lines to the file itself! First we want the headers, so we call .writeheader() on the writer object. This writes all the fields passed to fieldnames as the first row in our file. Then we iterate through our big_list of data. Each item in big_list is a dictionary with each field in fields as the keys. We call output_writer.writerow() with the item dictionaries which writes each line to the CSV file.


access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
with open('logger.csv','w') as logger_csv:
#Create a csv.DictWriter instance called log_writer. Pass logger_csv as the first argument and then fields as a keyword argument to the keyword fieldnames.
  log_writer = csv.DictWriter (logger_csv, fieldnames=fields )

  log_writer.writeheader()
  for element in access_log:
    log_writer.writerow(element)

 ######### Reading a JSON File

#We can also use Python’s file tools to read and write JSON. JSON, an abbreviation of JavaScript Object Notation, is a file format inspired by the programming language JavaScript. 

#import json
 
#with open('purchase_14781239.json') as purchase_json:
#  purchase_data = json.load(purchase_json)
 
#print(purchase_data['user'])

#First we import the json package. We opened the file using our trusty open() command. Since we’re opening it in read-mode we just need to pass the file name. We save the file in the temporary variable purchase_json.

#We continue by parsing purchase_json using json.load(), creating a Python dictionary out of the file. Saving the results into purchase_data means we can interact with it. We print out one of the values of the JSON file by keying into the purchase_data object

import json

with open('message.json') as message_json:
  message = json.load(message_json)

print(message['text'])

############### Writing a JSON File

#Naturally we can use the json library to translate Python objects to JSON as well. 
#This is especially useful in instances where you’re using a Python library to serve web pages, you would also be able to serve JSON. 
#import json
 
#with open('output.json', 'w') as json_file:
#  json.dump(turn_to_json, json_file)

#We import the json module, open up a write-mode file under the variable json_file, and then use the json.dump() method to write to the file. json.dump() takes two arguments: first the data object, then the file object you want to save.

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open('data.json','w') as data_json:
  json.dump(data_payload, data_json)





