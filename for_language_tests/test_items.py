import pytest

from selenium.webdriver.common.by import By
import time




def test_guest_should_see_basket_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    browser.get(link)

    time.sleep(30)
    
    assert browser.find_elements(By.CLASS_NAME,'btn-add-to-basket'),'No basket btn!'

if __name__ == "__main__":
    pytest.main()    