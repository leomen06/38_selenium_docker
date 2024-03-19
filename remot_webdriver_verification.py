from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor="http://localhost:4444", options=options)

driver.get("https://www.finning.com/en_CA.html")
html = driver.page_source
driver.quit()
