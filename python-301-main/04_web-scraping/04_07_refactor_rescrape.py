# Refactor your web scraping script and wrap all the functionality into
# separate functions. This is a great exercise to revisit writing functions
# as well as for refactoring your code. It'll also help you in an upcoming
# section of the course when you'll write tests for your web scraper.

import requests
from bs4 import BeautifulSoup
from pathlib import Path

def soup_web(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.text,"html.parser")

    return soup

def write_file(path,soup):
    data_path=Path(path)
    with open(data_path.joinpath("El_nino_web_scraping.txt"), "a",encoding="utf-8") as file:
        file.write(str(soup.find_all("p")))


def read_file(path):
    data_path=Path(path)
    with open(data_path.joinpath("El_nino_web_scraping.txt"), "r",encoding="utf-8") as file_in:
        soup1=BeautifulSoup(file_in,"html.parser")
        print(soup1.find("p"))




write_file("/Users/sagar/OneDrive/Escritorio",soup_web("https://public.wmo.int/en/our-mandate/climate/el-ni%C3%B1ola-ni%C3%B1a-update"))

read_file("/Users/sagar/OneDrive/Escritorio")



