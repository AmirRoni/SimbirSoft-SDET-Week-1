from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://automationteststore.com/"

    SEARCH_INPUT = (By.ID, "filter_keyword")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".button-in-search")

    def open(self):
        super().open(self.URL)

    def search(self, text: str):
        self.type(self.SEARCH_INPUT, text)
        self.click(self.SEARCH_BUTTON)
