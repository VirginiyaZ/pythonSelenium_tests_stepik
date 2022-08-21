import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAll(unittest.TestCase):

    def test_check_registration1(self):
        self.browser = browser.get(
            "http://suninjuly.github.io/registration1.html"
        )

        self.first = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first"
        ).send_keys("Data")

        self.second = browser.find_element(By.CSS_SELECTOR,
            "div.first_block input.second"
        ).send_keys("Data")

        self.third = browser.find_element(By.CSS_SELECTOR,
            "div.first_block input.third"
        ).send_keys("Data")

        self.button = browser.find_element(By.CSS_SELECTOR,
            "button.btn"
        ).click()

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!",
                         browser.find_element(By.TAG_NAME, "h1").text
                         )

    def test_check_registration2(self):
        self.browser = browser.get(
            "http://suninjuly.github.io/registration2.html"
        )

        self.first = browser.find_element(By.CSS_SELECTOR,
            "div.first_block input.first"
        ).send_keys("Data")

        self.second = browser.find_element(By.CSS_SELECTOR,
            "div.first_block input.second"
        ).send_keys("Data")

        self.third = browser.find_element(By.CSS_SELECTOR,
            "div.first_block input.third"
        ).send_keys("Data")

        self.button = browser.find_element(By.CSS_SELECTOR,
            "button.btn"
        ).click()

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!",
                         browser.find_element(By.TAG_NAME, "h1").text
                         )


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    unittest.main()