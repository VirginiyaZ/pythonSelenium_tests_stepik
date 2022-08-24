from selenium.webdriver.common.by import By

link_lst = ["http://selenium1py.pythonanywhere.com/"]

def test_guest_should_see_login_link(browser):
    browser.get(link_lst)
    browser.find_element(By.CSS_SELECTOR, "#login_link")