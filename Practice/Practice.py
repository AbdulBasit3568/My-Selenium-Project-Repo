from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

driver.maximize_window()
driver.get("https://cloud.tarsil.pk/")

wait.until(EC.visibility_of_element_located((By.ID, "txtUserName_Login"))).send_keys("admin@pani1")
driver.find_element(By.ID, "txtPassword_Login").send_keys("Basit@123")
driver.find_element(By.ID, "btnLogin_Login").click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Operations']"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "aSale_Index"))).click()

input("Sale page is opened. Press Enter to close the browser...")
driver.quit()
