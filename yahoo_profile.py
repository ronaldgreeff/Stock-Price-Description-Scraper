from bs4 import BeautifulSoup as bsoup
import urllib2
import re

# print(row[0])

data_symbol = "AMAT"
profile_url = "https://finance.yahoo.com/quote/%s/profile?p=%s"
profile = profile_url % (data_symbol, data_symbol)

profilepage = urllib2.urlopen(profile)
profilesoup = bsoup(profilepage,'html.parser')
 
description = profilesoup.find('section', 'quote-sub-section Mt(30px)').find_all('p')

print description[0].get_text()