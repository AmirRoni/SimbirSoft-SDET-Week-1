from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://automationteststore.com/"

    def open(self):
        super().open(self.URL)
