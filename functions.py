import bs4
import urllib

def search_terms_to_urls(search_terms):
	urls = []
	for term in search_terms:
		url = "https://www.jstor.org/dfr/results?Query=" + urllib.parse.quote(term, safe='')
		urls.append(url)
	return urls
	
def get_data_from_text(text,data_file,n,url):
	soup = bs4.BeautifulSoup(text)
	if soup.find("html") is None:
		totalresults = 'URL Error\n'
		print("Couldn't parse html file")
		print(soup)
	elif soup.find("h1") is None:
		totalresults = '0'
		print("Couldn't find header in html file")
	else:
		totalresults = soup.find("h1").get_text(strip=True)
	f = open(data_file, 'a')
	f.write('"' + totalresults + '","' + url + '"' + '\n')
	f.close()
	print(n)
	print(totalresults + '\n')
	print(url + '\n')