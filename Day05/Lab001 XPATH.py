# XPATH (Most Important Locator)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@value='radio2']").click()   # Syntax //tagname[@attribute='value']
time.sleep(2)                                                      #Check Uniqueness $x("//tagname[@attribute='value']")
driver.quit()