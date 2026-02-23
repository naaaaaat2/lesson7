
import time
import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator_operation(driver):
    page = CalculatorPage(driver)
    driver.get("https://bonigarcia.dev/"
               "selenium-webdriver-java/slow-calculator.html")
    page.set_delay(45)
    page.press_button("7")
    page.press_button("+")
    page.press_button("8")
    page.press_button("=")

    # Ждём 45 секунд, пока результат обновится
    time.sleep(45)

    result = page.get_result()
    assert result == "15", f"Ожидали 15, но получили {result}"
