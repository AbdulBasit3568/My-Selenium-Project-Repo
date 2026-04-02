# Start with (Attribute kis word se start ho raha hai.) Starting value constant ha
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
a = driver.find_element(By.XPATH,"//option[starts-with(@value,'option')]").text
print(a)
time.sleep(5)