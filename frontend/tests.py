# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class NiezapominkaTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://test.niezapominka/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_niezapominka(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Nie ma zada[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("new_task_name").clear()
        driver.find_element_by_name("new_task_name").send_keys("abc")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*abc[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("ol > li:first-child > div.task_div > button.delete_button").click()
        # Warning: verifyTextNotPresent may require manual changes
        try: self.assertNotRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*abc[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
