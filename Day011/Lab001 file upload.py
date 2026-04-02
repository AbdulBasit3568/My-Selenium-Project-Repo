# File Upload
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")
driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:\\Users\\HP\\Pictures\\Screenshots\\Screenshot 2026-03-31 174944.png")
driver.find_element(By.XPATH,"//input[@id='file-submit']").click()
time.sleep(5)