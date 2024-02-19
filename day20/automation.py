# Selenium pacakage

# to select browser 
# driver = webdriver.chrome()

# to select the website
# driver.get("google.com")'

#  to close 
# driver.close()

from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

input_element = driver.find_element(By.CLASS_NAME,'gLFyf')
input_element.send_keys("Python Tutorial"+KeysView.RETURN)

time.sleep(15)
driver.close()