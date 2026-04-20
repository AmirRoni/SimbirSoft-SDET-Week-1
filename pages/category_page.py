from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class CategoryPage(BasePage):
    PATH = "/index.php?rt=product/category&path=68"

    SORT_SELECT = (By.ID, "sort")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".fixed_wrapper")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".fixed_wrapper .prdocutname")

    def get_product_names(self) -> list[str]:
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        texts = []

        for element in elements:
            text = element.text.strip()
            if text:
                texts.append(text)
        return texts

    def get_product_prices(self) -> list[float]:
        cards = self.driver.find_elements(*self.PRODUCT_CARDS)
        prices = []

        for card in cards:
            new_price = card.find_elements(By.CSS_SELECTOR, ".pricenew")
            one_price = card.find_elements(By.CSS_SELECTOR, ".oneprice")

            if new_price:
                price_text = new_price[0].text.strip()
            elif one_price:
                price_text = one_price[0].text.strip()
            else:
                continue

            normalized_price = price_text.replace("$", "").strip()
            prices.append(float(normalized_price))

        return prices

    def select_sort_by_value(self, value: str):
        sort_element = self.find(self.SORT_SELECT)
        Select(sort_element).select_by_value(value)

    def sort_by_name_asc(self):
        self.select_sort_by_value("pd.name-ASC")

    def sort_by_name_desc(self):
        self.select_sort_by_value("pd.name-DESC")

    def sort_by_price_asc(self):
        self.select_sort_by_value("p.price-ASC")

    def sort_by_price_desc(self):
        self.select_sort_by_value("p.price-DESC")
