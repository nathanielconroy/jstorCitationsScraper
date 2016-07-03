# Open a text file containing a series of jstor search urls, separated by semicolons.
# Then read the file and split it into a list of the urls.
e = open('jstorurls.txt', 'r')
urlList = e.read()
urlList = urlList.split(";")

import requests
import bs4

# Open a file where the results of the scrape will be kept and delete its contents if any.
f = open('jstordataoutput.csv', 'w')
f.close()

# Cycle through all of the urls and scrape the total number of results for each search term.
# The script will print the results one by one and also write them into the jstordataoutput.csv file.
n = 0
for x in urlList:
	rawhtml = requests.get(x)
	soup = bs4.BeautifulSoup(rawhtml.text)
	if soup.find("html") is None:
		pressenter = raw_input('Error: Press Enter to Continue')
		totalresults = 'URL Error\n'	
	elif soup.find("h1") is None:
		totalresults = '0'
	else:
		totalresults = soup.find("h1").get_text(strip=True)
	f = open('jstordataoutput.csv', 'a')
	f.write('"' + totalresults + '","' + x + '"' + '\n')
	f.close()
	print(n)
	print(totalresults + '\n')
	print(x + '\n')