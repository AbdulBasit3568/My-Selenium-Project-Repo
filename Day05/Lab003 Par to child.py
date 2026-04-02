# Parent to Child
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']").click() #Attribute & Value
driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']/option[4]").click() # Parent to Child  # Syntax: //tagname[@attribute = 'value']/tagname
time.sleep(2)