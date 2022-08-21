import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# link = ' http://suninjuly.github.io/selects1.html'

link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)


x = browser.find_element(By.ID, "num1")
res_x = x.text
y = browser.find_element(By.ID, "num2")
res_y = y.text
sum_res = int(res_x)+ int(res_y)
print(sum_res)


select_num = Select(browser.find_element(By.TAG_NAME, "select"))
select_num.select_by_value(value=str(sum_res))


submit_btn = browser.find_element(By.XPATH, '//button[contains(@type,"submit")]')
submit_btn.click()
time.sleep(5)

browser.quit()