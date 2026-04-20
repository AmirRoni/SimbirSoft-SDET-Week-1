import random


def test_cart_validation(home_page, product_page, cart_page):
    home_page.open()

    product_names = home_page.get_product_names()
    assert len(product_names) >= 5, "На главной странице должно быть минимум 5 товаров"

    selected_indexes = random.sample(range(len(product_names)), 5)

    for index in selected_indexes:
        home_page.open()
        home_page.open_product_by_index(index)

        product_page.select_required_options()

        quantity = random.randint(1, 6)
        product_page.set_quantity(quantity)
        product_page.add_to_cart()

    cart_items_before = cart_page.get_cart_items()
    assert len(cart_items_before) == 5, "В корзине должно быть 5 разных товаров"

    cart_page.remove_even_items()

    updated_items = cart_page.get_cart_items()

    expected_items_total = sum(
        item["unit_price"] * item["quantity"] for item in updated_items
    )
    shipping = cart_page.get_shipping()
    expected_total = expected_items_total + shipping
    actual_total = cart_page.get_total()

    assert round(actual_total, 2) == round(expected_total, 2), "Итоговая стоимость корзины рассчитана неверно"
