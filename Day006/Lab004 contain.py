# Contain (Agar attribute ya text ka kuch hissa match karta ho to element select ho jaye.) value bs contain honi chahiyea.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

a = driver.find_element(By.XPATH,"//a[contains(@id,'open')]").text
print(a)

time.sleep(5)
driver.quit()