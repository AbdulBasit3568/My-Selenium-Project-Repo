#Text Element ka jo text page par likha hai us se element find karna.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
a = driver.find_element(By.XPATH,"//legend[text()='Checkbox Example']").text    # Syntax:  //tagname[text() = 'type text here']
print(a)
time.sleep(5)