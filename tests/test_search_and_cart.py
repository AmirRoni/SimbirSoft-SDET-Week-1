import random
from time import sleep

from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.product_page import ProductPage


def test_search_and_cart(driver):
    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    product_page = ProductPage(driver)

    home_page.open()
    home_page.search("shirt")

    search_page.sort_by_name_asc()

    for product_index in [1, 2]:
        search_page.open_product_by_index(product_index)

        quantity = random.randint(1, 6)
        product_page.set_quantity(quantity)
        product_page.add_to_cart()

        driver.back()
        sleep(1)
        driver.back()
        sleep(1)

    assert "Search"
