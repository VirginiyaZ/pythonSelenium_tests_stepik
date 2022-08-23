from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import time
import math

browser = webdriver.Chrome()

browser.get(" http://suninjuly.github.io/explicit_wait2.html")

try:

# говорим Selenium проверять в течение 10 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element(By.ID, "book")
    button.click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_val = browser.find_element(By.ID, "answer")
    input_val.send_keys(y)

    submit_btn = browser.find_element(By.XPATH, '//button[contains(@type,"submit")]')
    submit_btn.click()
    

finally:
    time.sleep(5)
    browser.quit()
