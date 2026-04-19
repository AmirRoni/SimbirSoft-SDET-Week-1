from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    QUANTITY_PRODUCT = (By.ID, "product_quantity")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".cart")

    def set_quantity(self, quantity: int):
        self.type(self.QUANTITY_PRODUCT, str(quantity))

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
