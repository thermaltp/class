import requests
from bs4 import BeautifulSoup
url = 'https://pastebin.com/archive'
#url = 'https://www.yelp.com/search?find_desc=&find_loc=Augusta+GA'
paste_r = requests.get(url)
print(paste_r)
#paste_r = (paste_r.text)
soup = BeautifulSoup(paste_r.text, 'html.parser')
#print(soup.findAll('a'))
#for link in soup.findAll('a'):
#    print(link)

#for name in soup.findAll('a', {'class': 'biz-name'}):
#    print(name.text)
for name in soup.findAll('table', {'class': 'maintable'}):
    print(name.text)