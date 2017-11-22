#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bs4
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://finance.yahoo.com/screener/predefined/undervalued_growth_stocks"
profile_url = "https://finance.yahoo.com/quote/%s/profile?p=%s"

loadpage = uReq(my_url)
showloadpage = loadpage.read()
loadpage.close()

soupit = soup(showloadpage, "html.parser")

#containers: <tr>
containers = soupit.findAll("tr", {"class" : re.compile("data-row.*")})

filename = "stocks.csv"
f = open(filename, "w")

headers = "name, description\n"

f.write("headers")

#loop through each container
for container in containers:
	#links: Fw(b) tags in <a>
	links = container.findAll("a", {"class" : "Fw(b)"})
	for link in links:
		data_symbol = link.get("data-symbol")
		for profile in link:
			profile = profile_url % (data_symbol, data_symbol)
			loadpage = uReq(profile)
			showpage = loadpage.read()
			loadpage.close()
			soupit = soup(showpage, "html.parser")
			name = soupit.find("h1").text
			description = soupit.find("p", {"class" : "Mt(15px) Lh(1.6)"}).text

	f.write(name + "," + description + "\n") #product_name.replace(",", "|") gets rid of a comma that's in the html being scraped
f.close()