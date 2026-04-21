import pytest
import allure
from selenium import webdriver

from pages.home_page import HomePage
from pages.category_page import CategoryPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"{item.name}_screenshot",
                attachment_type=allure.attachment_type.PNG
            )


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
