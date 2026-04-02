# start with and contains
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[starts-with(@id,'nam') and contains (@name,'er-n')]").click()
time.sleep(5)