from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
# using my url instead

my_url = "https://ss64.com/bash/"
uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()

# parsing the html
page_soup = soup(page_html, 'html parser')

# grabbing all containers with class name = item-container
containers = page_soup.findAll('div', {'class''item-container'})

# this is messy, apparently from my system the word link was unresolved so I troubleshooted doing this.
linksToFollow = []
for linksToFollow in linksToFollow:
    link_url = linksToFollow["href"]
    if link_url != "https://en.wikipedia.org/wiki/Expect":  # Im leaving this unchanged so we can figure this out.
        linksToFollow.append(my_url + link_url)
    else:
        linksToFollow.append(link_url)


filename = "bash_command_data.txt"
f = open(filename, 'w')
f.close()
