from selenium.webdriver.common.by import By
import time

def test_check_add_to_basket_btn(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket"), "Element is not found"