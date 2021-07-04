from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
# using my url instead

my_url ="https://ss64.com/bash/"
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# parsing the html
page_soup = soup(page_html, 'html parser')

# grabbing all containers with class name = item-container
containers = page_soup.findAll('div', {'class''item-container'})

my_url = "https://en.wikipedia.org/wiki/Expect"
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

filename = "bash_command_data.txt"
f = open(filename, 'w')

f.close()


