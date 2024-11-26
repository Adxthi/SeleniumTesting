from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.headless = False

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
time.sleep(5)
element=driver.find_element(By.ID, "contentLayout")
if element:
    print("Element is:",element)
    print("element found")
else:
    print("element not found")



driver.close()