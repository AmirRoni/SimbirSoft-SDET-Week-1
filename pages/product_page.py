from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, ".bgnone h1 span")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".productfilneprice")
    QUANTITY_PRODUCT = (By.ID, "product_quantity")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".cart")

    def get_product_name(self) -> str:
        return self.get_text(self.PRODUCT_NAME).strip()

    def get_product_price(self) -> float:
        text = self.get_text(self.PRODUCT_PRICE).replace("$", "").replace(",", "").strip()
        return float(text)

    def set_quantity(self, quantity: int):
        self.type(self.QUANTITY_PRODUCT, str(quantity))

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
