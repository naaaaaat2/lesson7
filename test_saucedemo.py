
import pytest
from selenium import webdriver
from LoginPage import LoginPage
from ProductsPage import ProductsPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_login_and_add_to_cart(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_to_cart("Sauce Labs Backpack")
