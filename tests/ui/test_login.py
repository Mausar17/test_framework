from pages.login_page import LoginPage

def test_valid_login_lands_on_inventory_page(driver):
    login_page = LoginPage(driver)
    inventory_page = login_page.open().login_expecting_success("standard_user","secret_sauce")
    assert inventory_page.is_loaded()
    assert inventory_page.get_page_title() == "Products"

def test_valid_login_shows_inventory_items(driver):
    login_page = LoginPage(driver)
    inventory_page = login_page.open().login_expecting_success("standard_user","secret_sauce")

    assert inventory_page.get_item_count() > 0

def test_invalid_login_shows_error_message(driver):
    login_page = LoginPage(driver)
    result = login_page.open().login("standard_user","wrong_password")

    assert result.has_error_message()
    assert "Username and password do not match" in result.get_error_message()