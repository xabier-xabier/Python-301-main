import pytest
import rescrape


def test_get_page_info():
    assert rescrape.get_page_content("https://codingnomads.github.io/recipes/").status_code==200
    assert rescrape.get_page_content("https://codingnomads.github.io/recipes/recipes/11-making-my-own-baguet.html").status_code==200

def test_web_content():
    assert ("<!DOCTYPE html>" in rescrape.get_html_content("https://codingnomads.github.io/recipes/"))
    assert ("<!DOCTYPE html>" in rescrape.get_html_content("https://codingnomads.github.io/recipes/recipes/11-making-my-own-baguet.html"))
       

def test_soup_creation_verf():
    html = rescrape.get_html_content("https://codingnomads.github.io/recipes/recipes/11-making-my-own-baguet.html")
    soup = rescrape.make_soup(html)
    assert "<class 'bs4.BeautifulSoup'>" == str(type(soup))

def test_index_check():
    index_html = rescrape.get_html_content("https://codingnomads.github.io/recipes/")
    index_soup = rescrape.make_soup(index_html)
    length=len(rescrape.get_recipe_links(index_soup))
    assert length > 0

def test_recipe_link():
    index_html = rescrape.get_html_content("https://codingnomads.github.io/recipes/")
    index_soup = rescrape.make_soup(index_html)
    assert (len(rescrape.get_recipe_links(index_soup))> 0)

def test_check_author():
    html = rescrape.get_html_content("https://codingnomads.github.io/recipes/recipes/11-making-my-own-baguet.html")
    soup = rescrape.make_soup(html)
    author = rescrape.get_author(soup)
    assert len(author)!=0
    assert "Jadafaa" == author

def test_get_recipe():
    html = rescrape.get_html_content("https://codingnomads.github.io/recipes/recipes/11-making-my-own-baguet.html")
    soup = rescrape.make_soup(html)
    recipe = rescrape.get_recipe(soup)
    assert type(recipe)== str
    assert len(recipe) > 0