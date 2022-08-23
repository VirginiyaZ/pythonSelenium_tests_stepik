from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = " http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.NAME, "firstname")
    input_name.send_keys("Virginiya")

    input_surname = browser.find_element(By.NAME, "lastname")
    input_surname.send_keys("Zubar")

    input_email = browser.find_element(By.NAME, "email")
    input_email.send_keys("stepik@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_name = "file.txt" 
# /Users/vz/Desktop/folder/qa_selenium/file.txt
    file_path = os.path.join(current_dir, file_name)
    print(file_path)

    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)


    input4 = browser.find_element(By.XPATH, '//button[contains(@type,"submit")]')
    input4.click()
    time.sleep(3)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()