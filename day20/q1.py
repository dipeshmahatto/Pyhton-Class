
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.headless = True 

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://the-internet.herokuapp.com/login")
input_element = driver.find_element(By.ID,'username')
input_element.send_keys("tomsmith")
input_element2 = driver.find_element(By.ID,'password')
input_element2.send_keys("SuperSecretPassword!")



input_element3= driver.find_element(By.CLASS_NAME,'radius')
input_element3.click()

output = driver.find_element(By.CLASS_NAME,'subheader')
print(output.text)

logout= driver.find_element(By.CLASS_NAME,'radius')
logout.click()

time.sleep(35)
driver.close()