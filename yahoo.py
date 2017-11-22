from bs4 import BeautifulSoup as bsoup
import urllib2
import re

url = "file:///C:/Users/Ronald/Desktop/Desktop/Python/StockCh/YFSS.html"
profile_url = "https://finance.yahoo.com/quote/%s/profile?p=%s"

table_page = urllib2.urlopen(url)
soup = bsoup(table_page,'html.parser')

table = soup.find('table')

table_rows = table.find_all('tr')

for tr in table_rows:
	th = tr.find_all('th')
	td = tr.find_all('td')
	throw = [i.text for i in th]
	tdrow = [i.text for i in td]
	
	x = throw + tdrow
	
	data_symbol = x.pop(0)

	profile = profile_url % (data_symbol, data_symbol)

	profilepage = urllib2.urlopen(profile)
	profilesoup = bsoup(profilepage,'html.parser')
 
	description = profilesoup.find('section', 'quote-sub-section Mt(30px)').find_all('p')

	print description[0].get_text()