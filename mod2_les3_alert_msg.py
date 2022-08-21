import time 
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    activate_btn = browser.find_element(By.TAG_NAME, "button")
    activate_btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)


    input4 = browser.find_element(By.XPATH, '//button[contains(@type,"submit")]')
    input4.click()
    time.sleep(5)



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    print(browser.switch_to.alert.text)
    browser.quit()
    