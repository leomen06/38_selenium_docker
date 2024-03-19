from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Importante para correr python en el contenedor.
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

driver = webdriver.Remote(
    'http://localhost:4444/wd/hub',
    #queremos acceder al drive de crhome para seterarla en la siguiente variable.
    desired_capabilities=webdriver.DesiredCapabilities.CHROME
)
driver.maximize_window()
driver.get("https://www.w3schools.com/")
time.sleep(3)

print(driver.title)