#parent to last child
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']").click()
driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']/option[last()]").click()
time.sleep(5)