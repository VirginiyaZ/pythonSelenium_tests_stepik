import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_basket_presence(browser):
    browser.get(link)
    assert WebDriverWait(browser, 7).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")),
        "Нет кнопки добавить товар в корзину"), "Нет возможности добавить товар в корзину"

    # Check the basket presence and the language
    time.sleep(30)


if __name__ == "__main__":
    pytest.main()