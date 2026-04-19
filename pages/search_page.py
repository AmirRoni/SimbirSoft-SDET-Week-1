from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class SearchPage(BasePage):
    SORT_SELECT = (By.ID, "sort")
    PRODUCT_LINKS = (By.CSS_SELECTOR, ".fixed_wrapper .prdocutname")

    def sort_by_name_asc(self):
        sort_element = self.find(self.SORT_SELECT)
        Select(sort_element).select_by_value("pd.name-ASC")

    def open_product_by_index(self, index: int):
        products = self.driver.find_elements(*self.PRODUCT_LINKS)
        products[index].click()

    def get_product_names(self) -> list[str]:
        products = self.driver.find_elements(*self.PRODUCT_LINKS)
        product_names = []

        for product in products:
            name = product.text.strip()
            if name:
                product_names.append(name)

        return product_names
