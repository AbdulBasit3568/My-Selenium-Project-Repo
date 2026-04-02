# CSS SELECTOR LOCATOR (Jab hum element ko id,class,name say locate na kar paien to hum CSS SELECTOR ka use kerty han.
# syntax tagname[attribute='value']
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[value='radio1']").click() # Check Uniqueness: $("tagname[attribute='value']")  $("input[value='radio1']")
time.sleep(5)
driver.quit()