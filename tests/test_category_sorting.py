def test_category_sorting(category_page):
    category_page.open()

    product_names = category_page.get_product_names()
    assert len(product_names) >= 4, "В категории должно быть минимум 4 товара"

    category_page.sort_by_name_asc()
    names_asc = category_page.get_product_names()
    assert names_asc == sorted(names_asc), "Сортировка по имени по возрастанию работает неверно"

    category_page.sort_by_name_desc()
    names_desc = category_page.get_product_names()
    assert names_desc == sorted(names_desc, reverse=True), "Сортировка по имени по убыванию работает неверно"

    category_page.sort_by_price_asc()
    prices_asc = category_page.get_product_prices()
    assert prices_asc == sorted(prices_asc), "Сортировка по цене по возрастанию работает неверно"

    category_page.sort_by_price_desc()
    prices_desc = category_page.get_product_prices()
    assert prices_desc == sorted(prices_desc, reverse=True), "Сортировка по цене по убыванию работает неверно"
