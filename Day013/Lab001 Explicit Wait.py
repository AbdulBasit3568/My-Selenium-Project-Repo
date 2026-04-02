from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://chercher.tech/practice/implicit-wait-example")
driver.implicitly_wait(10) # agar isy 5 secound may b element mil rha ha to yea ctick kr dyga
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH,"//div[@id='q']/input[1]")))
driver.find_element(By.XPATH,"//div[@id='q']/input[1]").click()