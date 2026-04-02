from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://cloud.tarsil.pk")              # Navigator: ka matlab hai browser ko control karna / page change karna. E.g. driver.get("https://google.com")  .back() .forward() .refresh()
driver.maximize_window()
driver.find_element(By.ID, "txtUserName_Login").send_keys("admin@pani1")
driver.find_element(By.ID, "txtPassword_Login").send_keys("Basit@123") # Locator: Page k kisi element ko find karna. E.g. inputbox, button, dropdown, checkbox (By.ID , By.Name, By.XPATh, By.CSS_SELECTOR etc
driver.find_element(By.ID, "btnLogin_Login").click()                 # Action: ka matlab hai element milne ke baad us par kaam karna. .click(), send_key, clear(), .text use to copy text

# Browser ko 12 seconds ke liye open rakhein
time.sleep(12)
driver.quit()
