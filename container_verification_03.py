from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

path = './chromedriver-win64/chromedriver.exe'
r_path = "\\home\\compu_dell_ubuntu_01\\platzi\\pip_y_entornos_virtuales\\py-project\\38.1_selenium_docker\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()
driver.get("https://www.w3schools.com/")
time.sleep(3)

print(driver.title)