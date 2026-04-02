# Grand parent to child
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
a = driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table/tbody/tr[5]/td[2]").text
print(a)
time.sleep(10)