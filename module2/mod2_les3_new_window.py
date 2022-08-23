import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    activate_btn = browser.find_element(By.TAG_NAME, "button")
    activate_btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
    print(browser.switch_to.alert.text)
    time.sleep(10)
    
    browser.quit()
