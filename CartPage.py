
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_cart(self):
        self.driver.get("https://www.saucedemo.com/cart.html")

    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")
