# Implicit Wait (Jitna mumkin ho saky selenium process kerny k liyea utna wait kery ga 30 second)
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://chercher.tech/practice/implicit-wait-example")
driver.implicitly_wait(10) # agar isy 5 secound may b element mil rha ha to yea click kr dyga
driver.find_element(By.XPATH,"//div[@id='q']/input[1]")
driver.find_element(By.XPATH,"//div[@id='q']/input[3]")