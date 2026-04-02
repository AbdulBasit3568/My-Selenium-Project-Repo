from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://cloud.tarsil.pk")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.quit()