# Open a text file containing a series of jstor search urls, separated by semicolons.
# Then read the file and split it into a list of the urls.
# urls = raw_input("What is the path where the jstor URLs are stored?")
# datafile = raw_input("What is the path where the data will be stored?")
# e = open(urls, 'r')
# urlList = e.read()
# urlList = urlList.split(";")

# # Ask the user what record to start at.
# startNumber = raw_input("What number would you like to start at? Starting at '0' will erase any previous results.")
# urlList = urlList[int(startNumber):]
# if startNumber == '0':
	# # Open a file where the results of the scrape will be kept and delete its contents if any.
	# f = open(datafile, 'w')
	# f.close()

import functions
import requests
	
search_terms = ['"Toni Morrison" AND "Beloved"']
urls = functions.search_terms_to_urls(search_terms)
data_file = "output.csv"
start_number = 0;
	
# Cycle through all of the urls and scrape the total number of results for each search term.
# The script will print the results one by one and also write them into the jstordataoutput.csv file.
n = int(start_number)
for x in urls:
	n += 1
	rawhtml = requests.get(x)
	print(rawhtml.text)
	get_data_from_text(rawhtml.text, data_file,n,x)
