from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for i in checkboxes:
    if i == checkboxes[1]:
        pass
    else:
        i.click()

print(len(checkboxes))
time.sleep(5)
driver.quit()