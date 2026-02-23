from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def set_delay(self, delay_value):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay_value))

    def press_button(self, button_text):
        button = self.driver.find_element(
            By.XPATH,
            f"//button[text()='{button_text}']"
        )
        button.click()

    def get_result(self):
        result_display = self.driver.find_element(By.ID, "result")
        return result_display.text
