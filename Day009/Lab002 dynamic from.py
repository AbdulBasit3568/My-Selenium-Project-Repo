from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cleartrip.com/")
driver.find_element(By.XPATH,"//input[@placeholder='Where to?']").send_keys("Laho")
time.sleep(5)
to_airport = driver.find_elements(By.XPATH,"//div[@class='dropdown p-absolute t-13 ln-1 w-100p']/ul/li")
for airport in to_airport:
    if "Lahore" in airport.text:
        airport.click()
        time.sleep(5)
        pass
