# Look for a static website online that has some information that you're
# interested in. Follow the web-scraping steps described in the course to
# inspect, scrape, and parse the information.
# BE RESPECTFUL! Don't scrape sites that don't want to be scraped, and
# limit the amount of calls you make to their page by saving the response
# to a file, and parsing the content from that file.

import requests
from bs4 import BeautifulSoup
from pathlib import Path

URL = "https://public.wmo.int/en/our-mandate/climate/el-ni%C3%B1ola-ni%C3%B1a-update"


page = requests.get(URL)
soup = BeautifulSoup(page.text,"html.parser")


data_path=Path("/Users/sagar/OneDrive/Escritorio")
with open(data_path.joinpath("El_nino_web_scraping.txt"), "a",encoding="utf-8") as file:
    file.write(str(soup.find_all("p")))

with open(data_path.joinpath("El_nino_web_scraping.txt"), "r",encoding="utf-8") as file_in:
    soup1=BeautifulSoup(file_in,"html.parser")
    print(soup1.find("p"))
    #print(file_in.read())

