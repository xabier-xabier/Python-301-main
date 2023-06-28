# Write a unittest test suite to test the rescrape module

import unittest
import rescrape


class TestWeb(unittest.TestCase):

    def test_get_page_info(self):
        self.assertEqual(rescrape.get_page_content("https://codingnomads.github.io/recipes/").status_code,200)
        self.assertEqual(rescrape.get_page_content("https://codingnomads.github.io/recipes/recipes/11-making-my-own-baguet.html").status_code,200)


    def test_web_content(self):
        self.assertIn("<!DOCTYPE html>", rescrape.get_html_content("https://codingnomads.github.io/recipes/"))
        self.assertIn("<!DOCTYPE html>",  rescrape.get_html_content("https://codingnomads.github.io/recipes/recipes/11-making-my-own-baguet.html"))

    def test_soup_creation_verf(self):
        html = rescrape.get_html_content("https://codingnomads.github.io/recipes/recipes/11-making-my-own-baguet.html")
        soup = rescrape.make_soup(html)
        self.assertEqual("<class 'bs4.BeautifulSoup'>", str(type(soup)))

    def test_index_check(self):
        index_html = rescrape.get_html_content("https://codingnomads.github.io/recipes/")
        index_soup = rescrape.make_soup(index_html)
        self.assertGreater(len(rescrape.get_recipe_links(index_soup)), 0)

    def test_recipe_link(self):
        index_html = rescrape.get_html_content("https://codingnomads.github.io/recipes/")
        index_soup = rescrape.make_soup(index_html)
        self.assertGreater(len(rescrape.get_recipe_links(index_soup)), 0)

    def test_check_author(self):
        html = rescrape.get_html_content("https://codingnomads.github.io/recipes/recipes/11-making-my-own-baguet.html")
        soup = rescrape.make_soup(html)
        author = rescrape.get_author(soup)
        self.assertNotEqual(len(author), 0)
        self.assertEqual("Jadafaa", author)

    def test_get_recipe(self):
        html = rescrape.get_html_content("https://codingnomads.github.io/recipes/recipes/11-making-my-own-baguet.html")
        soup = rescrape.make_soup(html)
        recipe = rescrape.get_recipe(soup)
        self.assertIsInstance(recipe, str)
        self.assertGreater(len(recipe), 0)
