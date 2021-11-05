import requests
from bs4 import BeautifulSoup


r = requests.get("https://pythonizing.github.io/data/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
# print (c)

soup = BeautifulSoup(c, "html.parser")

# print(soup.prettify())

div_content = soup.find_all("div", {"class":"cities"})

# print(div_content[0])

# print(div_content[2])

h2_text = div_content[0].find_all("h2")[0].text
# print(h2_text)

for item in div_content:
	print(item.find_all("h2")[0].text)

for item in div_content:
	print(item.find_all("p")[0].text)

