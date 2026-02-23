
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ProductsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def add_to_cart(self, product_name):
        button = self.driver.find_element(
            By.XPATH,
            f"//div[text()='{product_name}']"
            "/ancestor::div[@class='inventory_item']//button"
        )
        button.click()
