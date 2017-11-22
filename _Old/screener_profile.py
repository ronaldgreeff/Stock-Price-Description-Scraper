profile_url = "https://finance.yahoo.com/quote/%s/profile?p=%s" % ("AMAT", "AMAT")

loadpage = uReq(profile)
showpage = loadpage.read()
loadpage.close()
soupit = soup(showpage, "html.parser")
name = soupit.find("h1").text
description = soupit.find("p", {"class" : "Mt(15px) Lh(1.6)"}).text

f.write(name + "," + description + "\n") #product_name.replace(",", "|") gets rid of a comma that's in the html being scraped
f.close()