import requests
from bs4 import BeautifulSoup

# base URL of the website
BASEURL = "https://ss64.com/bash/"

# get HTML code and finds all links
page = requests.get(BASEURL)
baseSoup = BeautifulSoup(page.content, "html.parser")
links = baseSoup.find("table").find_all("a")

# places all links on the base URL page into linksToFollow list
linksToFollow = []
for link in links:
    link_url = link["href"]
    if link_url != "https://en.wikipedia.org/wiki/Expect":  # "expect" ref page is weird and navigates to wiki
        linksToFollow.append(BASEURL + link_url)
    else:
        linksToFollow.append(link_url)

# navigates to each link and searches for header (h1) and other relevant data (pre) and puts them in data list
data = []
for link in linksToFollow:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    soup.prettify()
    h1 = soup.find("h1")
    pre = soup.find_all("pre")
    data.append("\n\n********************\n\n" + h1.text.strip() + "\n")
    for specials in pre:
        data.append(str(specials.text.strip()))

# writes data to txt file for easy reading
filename = "bash_command_data.txt"
with open(filename, "w") as f:
     for d in data:
         f.write(d)