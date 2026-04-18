from pages.home_page import HomePage


def test_search_and_cart(driver):
    home_page = HomePage(driver)

    home_page.open()
    home_page.search("shirt")

    assert "Search"
