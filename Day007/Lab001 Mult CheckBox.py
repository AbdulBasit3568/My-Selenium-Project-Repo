from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']") # Common Xpath nikalna ha

for i in checkboxes:
    i.click()
print(len(checkboxes))
time.sleep(3)
driver.quit()