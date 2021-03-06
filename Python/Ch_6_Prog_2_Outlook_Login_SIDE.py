# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
vars = {}
# Test name: outlook
# Step # | name | target | value | comment
# 1 | open | https://www.outlook.com
driver.get("https://www.outlook.com")
print("driver.get('https://www.outlook.com')")
# 2 | setWindowSize | 1152x728 |  | 
driver.set_window_size(1152, 728)
print("driver.set_window_size(1152, 728)")
driver.find_element(By.XPATH, "/html/body/header/div/aside/div/nav/ul/li[2]/a").click()
# 3 | type | id=i0116 | rahman.kalilur@outlook.com | 
driver.find_element(By.ID, "i0116").send_keys("rahman.kalilur@outlook.com")
# 5 | click | id=i0116 |  | 
driver.find_element(By.ID, "i0116").click()
driver.find_element(By.ID, "i0118").clear()
driver.find_element(By.ID, "i0118").send_keys("Nas4Far$")
# 8 | sendKeys | id=i0116 | ${KEY_ENTER} | 
driver.find_element(By.ID, "i0116").send_keys(Keys.ENTER)
# 9 | click | id=i0118 |  | 
# 10 | click | id=idSIButton9 |  | 
driver.find_element(By.ID, "idSIButton9").click()
# 11 | mouseOver | id=id__3 |  | 
element = driver.find_element(By.ID, "id__3")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 12 | click | id=id__3 |  | 
driver.find_element(By.ID, "id__3").click()
# 13 | mouseOut | id=id__3 |  | 
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
# 14 | mouseOver | id=id__3 |  | 
element = driver.find_element(By.ID, "id__3")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 15 | mouseOut | id=id__3 |  | 
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
# 16 | mouseOver | css=.ms-Button--default .root-60 |  | 
element = driver.find_element(By.CSS_SELECTOR, ".ms-Button--default .root-60")
actions = ActionChains(driver)
# 17 | click | css=.ms-Button--default .root-60 |  | 
driver.find_element(By.CSS_SELECTOR, ".ms-Button--default .root-60").click()
# 18 | click | css=.\_14ggU2yZvNol5U91gfmYQA > img |  | 
driver.find_element(By.CSS_SELECTOR, ".\\_14ggU2yZvNol5U91gfmYQA > img").click()
# 19 | mouseOver | css=.\_14ggU2yZvNol5U91gfmYQA > img |  | 
element = driver.find_element(By.CSS_SELECTOR, ".\\_14ggU2yZvNol5U91gfmYQA > img")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
# 20 | mouseOut | css=#O365_MainLink_MePhoto img |  | 
element = driver.find_element(By.CSS_SELECTOR, "body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
# 21 | click | id=meControlSignoutLink |  | 
driver.find_element(By.ID, "meControlSignoutLink").click()
# 22 | close |  |  | 
driver.close()
  
driver.quit()
