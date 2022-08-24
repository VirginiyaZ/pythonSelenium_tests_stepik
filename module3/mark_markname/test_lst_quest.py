import time
import math
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


# links = ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1",
#         "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
#         "https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1",
#         "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"
# ]
# answer = math.log(int(time.time()))


@pytest.mark.parametrize("my_links", ["236895","236896",
        "236897", "236898",
        "236899","236903",
        "236904", "236905"
])
class TestCase:
    def test_guest_should_see_link(self, browser, my_links):
        answer = str(math.log(int(time.time())))

        link = f"https://stepik.org/lesson/{my_links}/step/1"
        browser.get(link)

        textarea = browser.find_element(By.CSS_SELECTOR, " .textarea")
        textarea.send_keys(answer)
        time.sleep(5)

        submit_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        submit_button.click()

        welcome_text_elt = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Correct!" == welcome_text
        time.sleep(5)

if __name__ == "__main__":
    pytest.main()