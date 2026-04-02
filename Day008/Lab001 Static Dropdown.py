# Static DropDown (Asy dropdown jin par click kerty he suggestions aty han)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
drop_down = Select(driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']"))

drop_down.select_by_visible_text("Option3")
time.sleep(2)
drop_down.select_by_index(2)
time.sleep(2)
drop_down.select_by_value("option1")
time.sleep(2)

driver.quit()