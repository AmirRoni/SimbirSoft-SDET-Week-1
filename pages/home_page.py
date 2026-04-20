from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from data.data import TIMEOUT


class HomePage(BasePage):
    PATH = "/"

    SEARCH_INPUT = (By.ID, "filter_keyword")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".button-in-search")
    PRODUCT_LINKS = (By.CSS_SELECTOR, ".fixed_wrapper .prdocutname")

    def search(self, text: str):
        self.type(self.SEARCH_INPUT, text)
        self.click(self.SEARCH_BUTTON)

    def get_product_names(self) -> list[str]:
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_any_elements_located(self.PRODUCT_LINKS)
        )
        products = self.driver.find_elements(*self.PRODUCT_LINKS)

        names = []
        for product in products:
            name = product.text.strip()
            if name:
                names.append(name)

        return names

    def open_product_by_index(self, index: int):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_any_elements_located(self.PRODUCT_LINKS)
        )
        products = self.driver.find_elements(*self.PRODUCT_LINKS)
        products[index].click()
