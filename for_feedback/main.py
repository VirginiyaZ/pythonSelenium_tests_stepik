from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome() # хромдрайвер должен лежать рядом с main.py
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    input2.send_keys('Petrov')
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    input3.send_keys('email@email.c')
    input4 = browser.find_element(By.CSS_SELECTOR, '.second_block .first')
    input4.send_keys("7900000000")
    input5 = browser.find_element(By.CSS_SELECTOR, '.second_block .second')
    input5.send_keys('Адрес')
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    button.click()

    time.sleep(2)
    welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()