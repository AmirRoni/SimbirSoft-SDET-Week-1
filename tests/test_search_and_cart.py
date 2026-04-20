import random


def test_search_and_cart(home_page, search_page, product_page, cart_page):

    for product_index in [1, 2]:
        home_page.open()
        home_page.search("shirt")

        search_page.sort_by_name_asc()

        search_page.open_product_by_index(product_index)

        quantity = random.randint(1, 6)
        product_page.set_quantity(quantity)
        product_page.add_to_cart()

    cart_items = cart_page.get_cart_items()
    print(cart_items)
    assert len(cart_items) >= 2, "В корзине должно быть минимум 2 товара"

    cheapest_item = cart_page.get_cheapest_item()
    new_quantity = cheapest_item["quantity"] * 2

    cart_page.set_quantity_by_name(cheapest_item["name"], new_quantity)
    cart_page.update_cart()

    updated_items = cart_page.get_cart_items()

    expected_items_total = sum(
        item["unit_price"] * item["quantity"] for item in updated_items
    )
    shipping = cart_page.get_shipping()
    expected_total = expected_items_total + shipping
    actual_total = cart_page.get_total()

    assert round(actual_total, 2) == round(expected_total, 2), "Итоговая стоимость корзины рассчитана неверно"
