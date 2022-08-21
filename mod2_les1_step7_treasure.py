import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
get_element = browser.find_element(By.ID, "treasure")
x_element = get_element.get_attribute("valuex")
x = x_element
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
time.sleep(2)
    

input2 = browser.find_element(By.ID, "robotCheckbox" )
input2.click()


input3 = browser.find_element(By.ID, "robotsRule")
input3.click()



input4 = browser.find_element(By.XPATH, '//button[contains(@type,"submit")]')
input4.click()
time.sleep(5)
    
browser.quit()
