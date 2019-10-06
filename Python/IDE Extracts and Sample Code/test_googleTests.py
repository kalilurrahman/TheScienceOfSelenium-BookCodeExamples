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

class TestGoogleTests():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
    self.driver.open("https://www.google.com")
    
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_test1(self):
    # Test name: Test_1
    # Step # | name | target | value | comment
    # 1 | click | name=q |  | 
    self.driver.find_element(By.NAME, "q").click()
    # 2 | type | name=q | testing | 
    self.driver.find_element(By.NAME, "q").send_keys("testing")
    # 3 | sendKeys | name=q | ${KEY_ENTER} | 
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    # 4 | mouseOver | id=uid_1 |  | 
    element = self.driver.find_element(By.ID, "uid_1")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 5 | mouseOut | id=uid_1 |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 6 | mouseOver | css=.NFQFxe:nth-child(2) .izHQgf |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".NFQFxe:nth-child(2) .izHQgf")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 7 | mouseOut | css=.NFQFxe:nth-child(2) .izHQgf |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 8 | click | css=.NFQFxe:nth-child(2) .RJn8N |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".NFQFxe:nth-child(2) .RJn8N").click()
    # 9 | click | linkText=Wikipedia |  | 
    self.vars["window_handles"] = self.driver.window_handles
    # 10 | storeWindowHandle | root |  | 
    self.driver.find_element(By.LINK_TEXT, "Wikipedia").click()
    # 11 | selectWindow | handle=${win9463} |  | 
    self.vars["win9463"] = self.wait_for_window(2000)
    # 12 | click | css=.tocsection-45 > a > .toctext |  | 
    self.vars["root"] = self.driver.current_window_handle
    # 13 | click | linkText=Test automation |  | 
    self.driver.switch_to.window(self.vars["win9463"])
    # 14 | click | css=.tocsection-5 .toctext |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".tocsection-45 > a > .toctext").click()
    # 15 | click | css=.thumbimage |  | 
    self.driver.find_element(By.LINK_TEXT, "Test automation").click()
    # 16 | mouseOver | css=.thumbimage |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".tocsection-5 .toctext").click()
    # 17 | runScript | window.scrollTo(0,0) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".thumbimage").click()
    # 18 | mouseOut | css=.thumbimage |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".thumbimage")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 19 | click | css=.mw-mmv-final-image |  | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 20 | click | css=body |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(driver)
    actions.move_to_element(element, 0, 0).perform()
    # 21 | close |  |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".mw-mmv-final-image").click()
    # 22 | selectWindow | handle=${root} |  | 
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    # 23 | assertTitle | title | Google | Test Google Title in Google Home Page
    self.driver.close()
    # 24 | doubleClickAt | xpath=//html[contains(.,'Preparing to run your test')] |  | 
    self.driver.switch_to.window(self.vars["root"])
    assert self.driver.title == "title"
    element = self.driver.find_element(By.XPATH, "//html[contains(.,\'Preparing to run your test\')]")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
  