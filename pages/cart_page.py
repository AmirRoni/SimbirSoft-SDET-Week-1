from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    URL = "https://automationteststore.com/index.php?rt=checkout/cart"

    CART_ROWS = (By.CSS_SELECTOR, ".cart-info.product-list table tbody tr")
    UPDATE_BUTTON = (By.ID, "cart_update")
    TOTAL_VALUE = (By.CSS_SELECTOR, "#totals_table td .totalamout")
    SUBTOTAL_VALUE = (By.CSS_SELECTOR, "#totals_table tr:first-child td:nth-child(2)")

    def open(self):
        super().open(self.URL)

    def parse_price(self, text: str) -> float:
        return float(text.replace("$", "").replace(",", "").strip())

    def get_cart_items(self) -> list[dict]:
        rows = self.driver.find_elements(*self.CART_ROWS)
        items = []

        for row in rows:
            quantity_inputs = row.find_elements(By.CSS_SELECTOR, "input[name*='quantity']")
            if not quantity_inputs:
                continue

            name = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) a").text.strip()
            unit_price_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text.strip()
            quantity = int(quantity_inputs[0].get_attribute("value"))
            total_price_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(6)").text.strip()

            items.append({
                "name": name,
                "unit_price": self.parse_price(unit_price_text),
                "quantity": quantity,
                "total_price": self.parse_price(total_price_text),
            })

        return items

    def get_cheapest_item(self) -> dict:
        items = self.get_cart_items()
        cheapest_item = items[0]

        for item in items:
            if item["unit_price"] < cheapest_item["unit_price"]:
                cheapest_item = item

        return cheapest_item

    def set_quantity_by_name(self, product_name: str, quantity: int):
        rows = self.driver.find_elements(*self.CART_ROWS)

        for row in rows:
            quantity_inputs = row.find_elements(By.CSS_SELECTOR, "input[name*='quantity']")
            if not quantity_inputs:
                continue

            name = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) a").text.strip()
            if name == product_name:
                quantity_input = quantity_inputs[0]
                quantity_input.clear()
                quantity_input.send_keys(str(quantity))
                return

        raise AssertionError(f"Товар '{product_name}' не найден в корзине")

    def update_cart(self):
        self.click(self.UPDATE_BUTTON)

    def get_subtotal(self) -> float:
        subtotal_text = self.get_text(self.SUBTOTAL_VALUE)
        return self.parse_price(subtotal_text)

    def get_total(self) -> float:
        totals = self.driver.find_elements(*self.TOTAL_VALUE)
        return self.parse_price(totals[-1].text)
