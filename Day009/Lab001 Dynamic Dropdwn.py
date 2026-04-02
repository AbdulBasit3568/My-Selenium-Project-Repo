# Dynamic Dropdown (assy dropdown hoty han jab type kro tab suggestion aty han)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.cleartrip.com/")

search_box = driver.find_element(By.XPATH,"//input[contains(@placeholder,'Where')]")
search_box.send_keys("dal")

time.sleep(3)

from_airport = driver.find_elements(By.XPATH,"//div[@class='dropdown p-absolute t-13 ln-1 w-100p']/ul/li")

for airport in from_airport:
    if "Dallas" in airport.text:
        airport.click()
        break

time.sleep(5)
driver.quit()

