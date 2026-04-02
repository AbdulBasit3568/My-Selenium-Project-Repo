# CSS Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Basit") # Check Uniqueness: tagname#IDvalue     input#name or #name
time.sleep(5)                                                   # Class  tagname.classvalue             .inputs
driver.quit()