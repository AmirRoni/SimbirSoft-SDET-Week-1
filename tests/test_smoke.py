from data.data import BASE_URL


def test_open_example(driver):
    driver.get(BASE_URL)
    assert "automation"
