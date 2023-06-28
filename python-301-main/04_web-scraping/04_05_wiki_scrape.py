# Write a web scraper that fetches the information from the Wikipedia page
# on Web scraping. Extract all the links on the page and filter them so the
# navigation links are excluded.
# Programmatically follow one of the links that lead to another Wikipedia article,
# extract the text content from that article, and save it to a local text file.
# BONUS TASK: Use RegExp to find all numbers in the text.
from random import randint
import requests
from bs4 import BeautifulSoup
from pathlib import Path



URL = "https://en.wikipedia.org/wiki/Web_scraping"
base="https://en.wikipedia.org/wiki/Web_scraping#bodyContent"

page = requests.get(URL)
soup = BeautifulSoup(page.text,"html.parser")


link_list=[]    # I will store all the links in this list

links = soup.find_all("a",href=True)
for link in links:
    link_list.append(link["href"])


for i in link_list:
    print(i)

# Extract all the links in the text

for a in soup.find_all('a', href=True):
    a.extract()

# Read all the paragraphs again (links already excluded)
paragraph = soup.find_all('p')

for each in paragraph:
    print (each.text)


new_base="https://en.wikipedia.org/"+link_list[link_list.index("/wiki/Data_scraping")]  

page1 = requests.get(new_base)
soup1 = BeautifulSoup(page1.text,"html.parser")


#for a in soup1.find_all('a', href=True):   We can extract the links again if we want
    #a.extract()

data_path=Path("/Users/sagar/OneDrive/Escritorio")
with open(data_path.joinpath("wikipedia_web_scraping.txt"), "a",encoding="utf-8") as file:
    file.write(str(soup1.find_all("p")))

