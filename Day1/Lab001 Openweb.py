from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.quit()