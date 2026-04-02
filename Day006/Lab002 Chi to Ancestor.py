# Child to any ancestor(Child element se uska parent ya upper element find karna.)  (Ismay hum child say parent he travel kar sakkty han child say kisi or parent k child tak access nhi kar sakty yea rule ha)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
a = driver.find_element(By.XPATH,"//option[@value='option3']/ancestor::div[@class='block large-row-spacer']").text
print(a)
time.sleep(5)