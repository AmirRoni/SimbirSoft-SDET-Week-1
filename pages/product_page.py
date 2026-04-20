from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

from random import choice


class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, ".bgnone h1 span")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".productfilneprice")
    QUANTITY_PRODUCT = (By.ID, "product_quantity")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".cart")

    PRODUCT_FORM = (By.ID, "product")
    OPTION_GROUPS = (By.CSS_SELECTOR, "#product .form-group")
    RADIO_LABELS = (By.CSS_SELECTOR, "label")
    SELECT_ELEMENTS = (By.TAG_NAME, "select")

    def get_product_name(self) -> str:
        return self.get_text(self.PRODUCT_NAME).strip()

    def get_product_price(self) -> float:
        text = self.get_text(self.PRODUCT_PRICE).replace("$", "").replace(",", "").strip()
        return float(text)

    def set_quantity(self, quantity: int):
        self.type(self.QUANTITY_PRODUCT, str(quantity))

    def select_required_options(self):
        groups = self.driver.find_elements(*self.OPTION_GROUPS)

        for group in groups:
            group_text = group.text.strip().lower()

            if not group_text:
                continue

            # radio
            radio_inputs = group.find_elements(By.CSS_SELECTOR, "input[type='radio']")
            if radio_inputs:
                valid_labels = []

                labels = group.find_elements(*self.RADIO_LABELS)
                for label in labels:
                    label_text = label.text.strip().lower()
                    if not label_text:
                        continue
                    if "out of stock" in label_text:
                        continue

                    related_inputs = label.find_elements(By.CSS_SELECTOR, "input[type='radio']")
                    if related_inputs and related_inputs[0].is_enabled():
                        valid_labels.append(label)

                if valid_labels:
                    random_label = choice(valid_labels)
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block: 'center'});", random_label
                    )
                    self.driver.execute_script("arguments[0].click();", random_label)
                    continue

            # select
            select_elements = group.find_elements(*self.SELECT_ELEMENTS)
            if select_elements:
                select = Select(select_elements[0])

                valid_options = [
                    option for option in select.options
                    if option.get_attribute("value")
                       and "select" not in option.text.lower()
                       and "out of stock" not in option.text.lower()
                ]

                if valid_options:
                    random_option = choice(valid_options)
                    select.select_by_value(random_option.get_attribute("value"))

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
