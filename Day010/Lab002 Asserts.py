# Assert (Yea hota ha Value confirm karwany k liyea k popup may jo value di ha actual may wo he ai the.)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Basit")
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
popup = driver.switch_to.alert
assert "Basit" in popup.text
popup.accept()