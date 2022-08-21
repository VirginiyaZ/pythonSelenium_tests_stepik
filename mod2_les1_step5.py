import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


link = 'https://suninjuly.github.io/math.html'

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
time.sleep(2)
    

input2 = browser.find_element(By.ID, "robotCheckbox" )
input2.click()


input3 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
input3.click()



input4 = browser.find_element(By.XPATH, '//button[contains(@type,"submit")]')
input4.click()
time.sleep(5)
    
browser.quit()



    
    