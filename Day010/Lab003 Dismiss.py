# Dismiss (Yea tab use hota ha jab popup may 1 say zyada selection button hon e.g. OK / Cancel)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Basit")
driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
popup = driver.switch_to.alert
time.sleep(5)
#popup.accept()
popup.dismiss()
time.sleep(5)