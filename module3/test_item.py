from selenium.webdriver.common.by import By



def test_guest_should_see_basket_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    assert browser.find_elements(By.CLASS_NAME,'btn btn-lg btn-primary btn-add-to-basket'),'Кнопка добавления товара в корзину отсутсвует'