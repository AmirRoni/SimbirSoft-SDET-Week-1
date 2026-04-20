import pytest
from selenium import webdriver

from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def category_page(driver):
    return CategoryPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture
def search_page(driver):
    return SearchPage(driver)
