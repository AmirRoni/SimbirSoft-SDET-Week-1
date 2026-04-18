from data.data import BASE_URL
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = BASE_URL

    def open(self):
        super().open(self.URL)
