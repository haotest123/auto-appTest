from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('AAAAAAAAAAAA')
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')  #注意这里组合键的输入。
time.sleep(10)
driver.quit()