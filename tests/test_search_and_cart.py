import random

from pages.home_page import HomePage
from pages.search_page import SearchPage


def test_search_and_cart(driver):
    home_page = HomePage(driver)
    search_page = SearchPage(driver)

    home_page.open()
    home_page.search("shirt")

    search_page.sort_by_name_asc()

    for product_index in [1, 2]:
        search_page.open_product_by_index(product_index)

        quantity = random.randint(1, 3)

    assert "Search"
