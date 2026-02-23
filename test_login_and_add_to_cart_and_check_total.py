from selenium import webdriver
from pages.saucedemo_login_page import LoginPage
from pages.saucedemo_products_page import ProductsPage
from pages.saucedemo_cart_page import CartPage
from pages.saucedemo_checkout import CheckoutPage


def test_login_and_add_to_cart_and_check_total():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(driver)
    products_page.add_backpack()
    products_page.add_tshirt()
    products_page.add_onesie()
    products_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    # Заполняем данными
    checkout_page.fill_form("Ivan", "Ivanov", "12345")

    # Получаем итоговую сумму
    total_price = checkout_page.get_total()

    # Проверяем итоговую сумму (указано, что нужно проверить)
    expected_total = 58.29  # сумма должна соответствовать реальной
    try:
        assert abs(total_price - expected_total) < 0.01, (
            f"Ожидали {expected_total}, получили {total_price}"
        )
        print("Итоговая сумма совпадает, тест прошёл успешно.")
    finally:
        driver.quit()
