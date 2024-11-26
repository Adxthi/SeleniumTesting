from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = False

# Set up the Chrome driver
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=Options())

driver.get("https://www.google.com/")
driver.find_element(By.NAME, "q").send_keys("Selenium")
driver.find_element(By.NAME, "q").submit()

driver.back()
time.sleep(3)
print("move to back page")

driver.forward()
time.sleep(3)
print("move to forward page")

driver.refresh()
time.sleep(3)
print("refresh the page")

driver.close()

