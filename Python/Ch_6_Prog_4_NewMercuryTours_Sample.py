# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:32:02 2019

@author: rahma
"""

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Mercury2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_mercury2(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com/")
        driver.find_element_by_name("userName").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='SIGN-ON'])[1]/following::td[1]").click()
        driver.find_element_by_link_text("REGISTER").click()
        driver.find_element_by_name("firstName").clear()
        driver.find_element_by_name("firstName").send_keys("Selenium")
        driver.find_element_by_name("lastName").clear()
        driver.find_element_by_name("lastName").send_keys("User")
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("1234567890")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("sel@eni.um")
        driver.find_element_by_name("address1").clear()
        driver.find_element_by_name("address1").send_keys("1234 5th avenue")
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("sixth street")
        driver.find_element_by_name("city").clear()
        driver.find_element_by_name("city").send_keys("denver")
        driver.find_element_by_name("state").clear()
        driver.find_element_by_name("state").send_keys("colorado")
        driver.find_element_by_name("postalCode").clear()
        driver.find_element_by_name("postalCode").send_keys("80231")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("seluser")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("seluser")
        driver.find_element_by_name("confirmPassword").clear()
        driver.find_element_by_name("confirmPassword").send_keys("seluser")
        driver.find_element_by_name("register").click()
        driver.find_element_by_link_text("sign-in").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/preceding::td[3]").click()
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("sel")
        driver.find_element_by_name("userName").send_keys(Keys.DOWN)
        driver.find_element_by_name("userName").send_keys(Keys.DOWN)
        driver.find_element_by_name("userName").send_keys(Keys.TAB)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("seluser")
        driver.find_element_by_xpath("//div").click()
     #   driver.find_element_by_name("login").click()
     #   driver.find_element_by_name("login").click()
        driver.find_element_by_link_text("Home").click()
     #   driver.find_element_by_name("userName").clear()
     #   driver.find_element_by_name("userName").send_keys("seluser")
     #   driver.find_element_by_name("password").clear()
     #   driver.find_element_by_name("password").send_keys("seluser")
     #   driver.find_element_by_name("login").click()
     #   driver.find_element_by_name("login").click()
        driver.find_element_by_link_text("Flights").click()
        driver.find_element_by_name("toDay").click()
        driver.find_element_by_name("toDay").click()
        Select(driver.find_element_by_name("toDay")).select_by_visible_text("15")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Returning:'])[1]/following::option[27]").click()
        driver.find_element_by_name("findFlights").click()
        driver.find_element_by_name("reserveFlights").click()
        driver.find_element_by_name("passFirst0").click()
        driver.find_element_by_name("passFirst0").clear()
        driver.find_element_by_name("passFirst0").send_keys("Selenium")
        driver.find_element_by_name("passLast0").clear()
        driver.find_element_by_name("passLast0").send_keys("User")
        Select(driver.find_element_by_name("pass.0.meal")).select_by_visible_text("Bland")
        Select(driver.find_element_by_name("pass.0.meal")).select_by_visible_text("Diabetic")
        Select(driver.find_element_by_name("pass.0.meal")).select_by_visible_text("Hindu")
        Select(driver.find_element_by_name("pass.0.meal")).select_by_visible_text("Kosher")
        Select(driver.find_element_by_name("pass.0.meal")).select_by_visible_text("Low Calorie")
        driver.find_element_by_name("creditnumber").clear()
        driver.find_element_by_name("creditnumber").send_keys("1234567890123456")
        Select(driver.find_element_by_name("cc_exp_dt_mn")).select_by_visible_text("01")
        Select(driver.find_element_by_name("cc_exp_dt_mn")).select_by_visible_text("02")
        Select(driver.find_element_by_name("cc_exp_dt_mn")).select_by_visible_text("03")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2000")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2001")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2002")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2003")
        self.assertEqual("You have entered 2003 as expiration year!", self.close_alert_and_get_its_text())
        driver.find_element_by_name("cc_exp_dt_yr").click()
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2010")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Expiration:'])[1]/following::option[31]").click()
        driver.find_element_by_name("cc_frst_name").click()
        driver.find_element_by_name("cc_frst_name").clear()
        driver.find_element_by_name("cc_frst_name").send_keys("Selenium")
        driver.find_element_by_name("cc_last_name").clear()
        driver.find_element_by_name("cc_last_name").send_keys("User")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CONTACT'])[1]/following::table[3]").click()
        driver.find_element_by_name("ticketLess").click()
        driver.find_element_by_name("buyFlights").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CONTACT'])[1]/following::img[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='$584 USD'])[1]/following::img[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Flights'])[1]/following::td[2]").click()
        driver.find_element_by_link_text("Hotels").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='© 2005, Mercury Interactive (v. 011003-1.01-058)'])[1]/preceding::img[1]").click()
        driver.find_element_by_link_text("Car Rentals").click()
     #   driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='© 2005, Mercury Interactive (v. 011003-1.01-058)'])[1]/preceding::img[1]").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Shipboard accomodations include: all meals, daily activities and nightly entertainment'])[1]/following::img[1]").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Preferences'])[1]/following::font[3]").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Preferences'])[1]/following::font[3]").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CONTACT'])[1]/following::table[3]").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Preferences'])[1]/following::font[3]").click()
        driver.find_element_by_name("findFlights").click()
        driver.find_element_by_name("reserveFlights").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cruises'])[1]/following::td[2]").click()
        driver.find_element_by_link_text("Cruises").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='© 2005, Mercury Interactive (v. 011003-1.01-058)'])[1]/preceding::img[1]").click()
        driver.find_element_by_link_text("Cruises").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Shipboard accomodations include: all meals, daily activities and nightly entertainment'])[1]/following::img[1]").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Preferences'])[1]/following::font[3]").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Preferences'])[1]/following::font[3]").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Preferences'])[1]/following::td[2]").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Airline:'])[1]/preceding::input[1]").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Airline:'])[1]/preceding::input[2]").click()
     #   driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Airline:'])[1]/preceding::input[1]").click()
        driver.find_element_by_name("passCount").click()
        Select(driver.find_element_by_name("passCount")).select_by_visible_text("4")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Passengers:'])[1]/following::option[4]").click()
        driver.find_element_by_name("toDay").click()
        Select(driver.find_element_by_name("toDay")).select_by_visible_text("19")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Returning:'])[1]/following::option[31]").click()
        driver.find_element_by_name("fromPort").click()
        Select(driver.find_element_by_name("fromPort")).select_by_visible_text("New York")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Passengers:'])[1]/following::option[8]").click()
        driver.find_element_by_name("toPort").click()
        Select(driver.find_element_by_name("toPort")).select_by_visible_text("Sydney")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='On:'])[1]/following::option[52]").click()
        driver.find_element_by_name("findFlights").click()
      #  driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Unified Airlines 363'])[1]/preceding::td[1]").click()
      #  driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Unified Airlines 363'])[1]/preceding::td[1]").click()
      #  driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Unified Airlines 363'])[1]/preceding::td[1]").click()
      #  driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Unified Airlines 363'])[1]/preceding::input[1]").click()
        driver.find_element_by_name("results").click()
      #  driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Unified Airlines 633'])[1]/preceding::td[1]").click()
       # driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Unified Airlines 633'])[1]/preceding::td[1]").click()
        driver.find_element_by_xpath("//td").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Unified Airlines 633'])[1]/preceding::input[1]").click()
        driver.find_element_by_name("reserveFlights").click()
        driver.find_element_by_name("passFirst0").click()
        driver.find_element_by_name("passFirst0").clear()
        driver.find_element_by_name("passFirst0").send_keys("Selenium")
        driver.find_element_by_name("passLast0").clear()
        driver.find_element_by_name("passLast0").send_keys("User")
        Select(driver.find_element_by_name("pass.0.meal")).select_by_visible_text("Bland")
        Select(driver.find_element_by_name("pass.0.meal")).select_by_visible_text("Diabetic")
        Select(driver.find_element_by_name("pass.0.meal")).select_by_visible_text("Bland")
        driver.find_element_by_name("passFirst1").clear()
        driver.find_element_by_name("passFirst1").send_keys("Sel")
        driver.find_element_by_name("passLast1").clear()
        driver.find_element_by_name("passLast1").send_keys("U2")
        Select(driver.find_element_by_name("pass.1.meal")).select_by_visible_text("Bland")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Last Name:'])[2]/following::td[1]").click()
        Select(driver.find_element_by_name("pass.1.meal")).select_by_visible_text("Diabetic")
        driver.find_element_by_name("passFirst2").clear()
        driver.find_element_by_name("passFirst2").send_keys("Sel")
        driver.find_element_by_name("passLast2").clear()
        driver.find_element_by_name("passLast2").send_keys("U3")
        Select(driver.find_element_by_name("pass.2.meal")).select_by_visible_text("Bland")
        Select(driver.find_element_by_name("pass.2.meal")).select_by_visible_text("Diabetic")
        Select(driver.find_element_by_name("pass.2.meal")).select_by_visible_text("Hindu")
        driver.find_element_by_name("passFirst3").clear()
        driver.find_element_by_name("passFirst3").send_keys("Sel")
        driver.find_element_by_name("passLast3").clear()
        driver.find_element_by_name("passLast3").send_keys("U4")
        Select(driver.find_element_by_name("pass.3.meal")).select_by_visible_text("Bland")
        Select(driver.find_element_by_name("pass.3.meal")).select_by_visible_text("Diabetic")
        Select(driver.find_element_by_name("pass.3.meal")).select_by_visible_text("Hindu")
        Select(driver.find_element_by_name("pass.3.meal")).select_by_visible_text("Kosher")
        Select(driver.find_element_by_name("pass.3.meal")).select_by_visible_text("Low Calorie")
        Select(driver.find_element_by_name("pass.2.meal")).select_by_visible_text("Kosher")
        Select(driver.find_element_by_name("pass.2.meal")).select_by_visible_text("Low Calorie")
        Select(driver.find_element_by_name("pass.2.meal")).select_by_visible_text("Low Cholesterol")
        driver.find_element_by_name("creditnumber").clear()
        driver.find_element_by_name("creditnumber").send_keys("123")
        driver.find_element_by_name("creditnumber").send_keys(Keys.DOWN)
        driver.find_element_by_name("creditnumber").send_keys(Keys.DOWN)
        driver.find_element_by_name("creditnumber").send_keys(Keys.DOWN)
        driver.find_element_by_name("creditnumber").send_keys(Keys.TAB)
        Select(driver.find_element_by_name("cc_exp_dt_mn")).select_by_visible_text("01")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2000")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2001")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2002")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2003")
        self.assertEqual("You have entered 2003 as expiration year!", self.close_alert_and_get_its_text())
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2004")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2005")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2006")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2007")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2008")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2009")
        Select(driver.find_element_by_name("cc_exp_dt_yr")).select_by_visible_text("2010")
        driver.find_element_by_name("cc_frst_name").clear()
        driver.find_element_by_name("cc_frst_name").send_keys("Selenium")
        driver.find_element_by_name("cc_last_name").clear()
        driver.find_element_by_name("cc_last_name").send_keys("User")
        driver.find_element_by_name("ticketLess").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Delivery Address'])[1]/following::input[1]").click()
        driver.find_element_by_name("buyFlights").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CONTACT'])[1]/following::img[3]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Vacations'])[1]/following::u[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Vacations'])[1]/following::u[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Use Java Version'])[1]/following::img[1]").click()
        driver.find_element_by_link_text("SUPPORT").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CONTACT'])[1]/following::td[7]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cruises'])[1]/following::td[2]").click()
        driver.find_element_by_xpath("//td/table/tbody/tr/td/table/tbody/tr/td/table").click()
        driver.find_element_by_link_text("Vacations").click()
        driver.find_element_by_xpath("//td/table/tbody/tr/td/table/tbody/tr/td").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Vacations'])[1]/following::img[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Use Java Version'])[1]/following::img[1]").click()
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
