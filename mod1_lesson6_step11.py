from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # линк1 для работы без ошибки
    # link = "http://suninjuly.github.io/registration1.html" 

    # линк2 для проверки теста с ошибкой
    link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH,"//input[contains(@class, 'first') and @required]")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH,"//input[contains(@class, 'second') and @required]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH,"//input[contains(@class, 'third') and @required]")
    input3.send_keys("sabaka@mail.com")
    time.sleep(7)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()