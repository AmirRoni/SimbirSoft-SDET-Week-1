from pages.home_page import HomePage


def test_open_example(driver):
    home_page = HomePage(driver)
    home_page.open()

    assert "automation"
