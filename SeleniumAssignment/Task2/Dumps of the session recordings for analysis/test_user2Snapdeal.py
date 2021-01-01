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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUser2Snapdeal():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_user2Snapdeal(self):
    self.driver.get("https://www.snapdeal.com/")
    self.driver.set_window_size(1051, 806)
    self.driver.find_element(By.ID, "inputValEnter").click()
    self.driver.find_element(By.ID, "inputValEnter").send_keys("samsung galaxy m21 ")
    self.driver.find_element(By.CSS_SELECTOR, ".currenthover > .subdiv").click()
    self.driver.execute_script("window.scrollTo(0,1800)")
    self.driver.find_element(By.ID, "inputValEnter").click()
    self.driver.find_element(By.ID, "inputValEnter").send_keys("samsung galaxy m21 mobile phone 64gb")
    self.driver.find_element(By.ID, "inputValEnter").send_keys(Keys.ENTER)
    self.driver.execute_script("window.scrollTo(0,16.799999237060547)")
    self.driver.find_element(By.CSS_SELECTOR, "#\\36 917529682576574946 > .product-tuple-description").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#\\36 917529682576574946 .product-title").click()
    self.vars["win9927"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win9927"])
    self.driver.find_element(By.CSS_SELECTOR, "#add-cart-button-id > .intialtext").click()
  
