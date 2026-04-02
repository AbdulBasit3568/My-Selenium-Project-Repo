from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.PARTIAL_LINK_TEXT, "Join Rahul Shetty for a QA").click()
a = driver.find_element(By.ID, "openwindow").text
print(a)

time.sleep(5)
driver.quit()