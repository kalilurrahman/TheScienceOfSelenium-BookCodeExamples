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

class TestBPBOnlineTestCases():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_bPBOnlineTestCases(self):
    # Test name: BPB Online Test Cases
    # Step # | name | target | value | comment
    # 1 | open | https://bpbonline.com/ |  | 
    self.driver.get("https://bpbonline.com/")
    # 2 | setWindowSize | 1050x708 |  | 
    self.driver.set_window_size(1050, 708)
    # 3 | click | id=bc-product-search |  | 
    self.driver.find_element(By.ID, "bc-product-search").click()
    # 4 | click | id=bc-product-search |  | 
    self.driver.find_element(By.ID, "bc-product-search").click()
    # 5 | type | id=bc-product-search | selenium | 
    self.driver.find_element(By.ID, "bc-product-search").send_keys("selenium")
    # 6 | click | id=search |  | 
    self.driver.find_element(By.ID, "search").click()
    # 7 | verifyTitle | Computer & IT Books | Emerging & Trending Technologies l E-books – BPB Publications |  | 
    assert self.driver.title == "Computer & IT Books | Emerging & Trending Technologies l E-books – BPB Publications"
    # 8 | click | css=.tt-cursor .text-search-sn-search-shopify |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".tt-cursor .text-search-sn-search-shopify").click()
    # 9 | type | id=bc-product-search | C Under DOS Test by Riku Parikh, Anup Jalan, Soham Desai | 
    self.driver.find_element(By.ID, "bc-product-search").send_keys("C Under DOS Test by Riku Parikh, Anup Jalan, Soham Desai")
    # 10 | mouseOver | css=.active:nth-child(4) > .dropdown-link > span |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".active:nth-child(4) > .dropdown-link > span")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 11 | assertText | css=span > strong | Description: | 
    assert self.driver.find_element(By.CSS_SELECTOR, "span > strong").text == "Description:"
    # 12 | click | css=.hover:nth-child(5) > a |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".hover:nth-child(5) > a").click()
    # 13 | click | id=bc-product-search |  | 
    self.driver.find_element(By.ID, "bc-product-search").click()
    # 14 | click | css=.hover span |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".hover span").click()
    # 15 | click | id=bc-product-search |  | 
    self.driver.find_element(By.ID, "bc-product-search").click()
    # 16 | type | id=bc-product-search | artif | 
    self.driver.find_element(By.ID, "bc-product-search").send_keys("artif")
    # 17 | click | id=bc-product-search |  | 
    self.driver.find_element(By.ID, "bc-product-search").click()
    # 18 | assertText | css=.tt-cursor .content-lineal-sn-search-shopify | Artificial Intelligence | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".tt-cursor .content-lineal-sn-search-shopify").text == "Artificial Intelligence"
    # 19 | click | css=.tt-cursor .tt-highlight |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".tt-cursor .tt-highlight").click()
    # 20 | type | id=bc-product-search | Artificial Intelligence | 
    self.driver.find_element(By.ID, "bc-product-search").send_keys("Artificial Intelligence")
    # 21 | click | css=.grid |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".grid").click()
    # 22 | mouseOver | css=.product-grid-item:nth-child(2) .featured-image |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(2) .featured-image")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 23 | click | css=.product-grid-item:nth-child(2) .featured-image |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".product-grid-item:nth-child(2) .featured-image").click()
    # 24 | storeTitle | AI & ML - Powering the Agents of Automation – BPB Publications | AIBook | 
    self.vars["AIBook"] = self.driver.title
    # 25 | click | id=add-to-cart |  | 
    self.driver.find_element(By.ID, "add-to-cart").click()
    # 26 | click | css=.action > .btn-default |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".action > .btn-default").click()
    # 27 | mouseDownAt | id=checkout_email_or_phone | 407.15625,24.015625 | 
    element = self.driver.find_element(By.ID, "checkout_email_or_phone")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 28 | mouseMoveAt | id=checkout_email_or_phone | 407.15625,24.015625 | 
    element = self.driver.find_element(By.ID, "checkout_email_or_phone")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # 29 | mouseUpAt | id=checkout_email_or_phone | 407.15625,24.015625 | 
    element = self.driver.find_element(By.ID, "checkout_email_or_phone")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    # 30 | click | id=checkout_email_or_phone |  | 
    self.driver.find_element(By.ID, "checkout_email_or_phone").click()
    # 31 | type | id=checkout_email_or_phone | abc@def.com | 
    self.driver.find_element(By.ID, "checkout_email_or_phone").send_keys("abc@def.com")
    # 32 | type | name=checkout[shipping_address][first_name] | Selenium | 
    self.driver.find_element(By.NAME, "checkout[shipping_address][first_name]").send_keys("Selenium")
    # 33 | type | name=checkout[shipping_address][last_name] | User | 
    self.driver.find_element(By.NAME, "checkout[shipping_address][last_name]").send_keys("User")
    # 34 | type | name=checkout[shipping_address][address1] | 12345, Sixth Street | 
    self.driver.find_element(By.NAME, "checkout[shipping_address][address1]").send_keys("12345, Sixth Street")
    # 35 | type | name=checkout[shipping_address][address2] | Seventh Avenue | 
    self.driver.find_element(By.NAME, "checkout[shipping_address][address2]").send_keys("Seventh Avenue")
    # 36 | type | name=checkout[shipping_address][city] | Denver | 
    self.driver.find_element(By.NAME, "checkout[shipping_address][city]").send_keys("Denver")
    # 37 | type | name=checkout[shipping_address][country] | US | 
    self.driver.find_element(By.NAME, "checkout[shipping_address][country]").send_keys("US")
    # 38 | type | name=checkout[shipping_address][province] | Colorado | 
    self.driver.find_element(By.NAME, "checkout[shipping_address][province]").send_keys("Colorado")
    # 39 | type | name=checkout[shipping_address][zip] | 80201 | 
    self.driver.find_element(By.NAME, "checkout[shipping_address][zip]").send_keys("80201")
    # 40 | type | name=checkout[shipping_address][phone] | 9876543241 | 
    self.driver.find_element(By.NAME, "checkout[shipping_address][phone]").send_keys("9876543241")
    # 41 | click | id=checkout_remember_me |  | 
    self.driver.find_element(By.ID, "checkout_remember_me").click()
    # 42 | click | css=.icon-svg--size-18 |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".icon-svg--size-18").click()
    # 43 | click | css=.btn__content |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn__content").click()
    # 44 | click | css=.radio-wrapper:nth-child(2) > .radio__label |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".radio-wrapper:nth-child(2) > .radio__label").click()
    # 45 | click | css=.shown-if-js > #continue_button > .icon-svg |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".shown-if-js > #continue_button > .icon-svg").click()
    # 46 | selectFrame | index=0 |  | 
    self.driver.switch_to.frame(0)
    # 47 | assertTitle | Razorpay Checkout |  | 
    assert self.driver.title == "Razorpay Checkout"
    # 48 | close |  |  | 
    self.driver.close()
  
