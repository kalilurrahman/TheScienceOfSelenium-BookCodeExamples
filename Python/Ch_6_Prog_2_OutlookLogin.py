# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
   #     self.driver.implicitly_wait(5)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://outlook.live.com/owa/")
        driver.find_element_by_link_text("Sign in").click()
        print("Success 1")
        driver.implicitly_wait(5)
        driver.find_element_by_id("i0116").click()
        driver.find_element_by_id("i0116").clear()
        driver.find_element_by_id("i0116").send_keys("rahman.kalilur@outlook.com" + Keys.ENTER)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Create one!'])[1]/preceding::div[5]").click()
        driver.find_element_by_id("idSIButton9").click()
        print("Success 2")
        driver.implicitly_wait(5)
        driver.find_element_by_id("i0118").click()
        driver.find_element_by_id("i0118").clear()
        driver.find_element_by_id("i0118").send_keys("Nas4Far$" + Keys.ENTER)
        driver.find_element_by_id("idSIButton9").click()
        print("Success 3")
        driver.implicitly_wait(5)
        driver.find_element_by_id("id__3").click()
        driver.find_element_by_id("id__992").click()
        print("Success 4")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='KR'])[1]/following::img[1]").click()
        driver.find_element_by_id("meControlSignoutLink").click()
        print("Success 5")
        driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
