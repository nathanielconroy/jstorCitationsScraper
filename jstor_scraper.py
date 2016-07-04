# Open a text file containing a series of jstor search urls, separated by semicolons.
# Then read the file and split it into a list of the urls.
urls = raw_input("What is the path where the jstor URLs are stored?")
datafile = raw_input("What is the path where the data will be stored?")
e = open(urls, 'r')
urlList = e.read()
urlList = urlList.split(";")

# Ask the user what record to start at.
startNumber = raw_input("What number would you like to start at? Starting at '0' will erase any previous results.")
urlList = urlList[int(startNumber):]
if startNumber == '0':
	# Open a file where the results of the scrape will be kept and delete its contents if any.
	f = open(datafile, 'w')
	f.close()

import requests
import bs4

# Cycle through all of the urls and scrape the total number of results for each search term.
# The script will print the results one by one and also write them into the jstordataoutput.csv file.
n = int(startNumber)
for x in urlList:
	n += 1
	rawhtml = requests.get(x)
	soup = bs4.BeautifulSoup(rawhtml.text)
	if soup.find("html") is None:
		pressenter = raw_input('Error: Press Enter to Continue')
		totalresults = 'URL Error\n'	
	elif soup.find("h1") is None:
		totalresults = '0'
	else:
		totalresults = soup.find("h1").get_text(strip=True)
	f = open(datafile, 'a')
	f.write('"' + totalresults + '","' + x + '"' + '\n')
	f.close()
	print(n)
	print(totalresults + '\n')
	print(x + '\n')
