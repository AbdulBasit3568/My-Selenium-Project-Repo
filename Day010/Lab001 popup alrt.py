from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Basit")
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
popup = driver.switch_to.alert # alert HTMl CSS ka part nhi hota isko inspect nhi kiyea ja sakta isi liyea hamain chrome ko switch krna parta ha taky focus alert par jay
time.sleep(2)
print(popup.text)
popup.accept() # hamarin yahan popup ko accept krwana parta ha

time.sleep(5)
driver.quit()