from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = False

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=Options())

driver.get("https://www.google.com")
element=driver.find_element(By.NAME, "q")
print("Element is:",element)
print("Element is:",element.tag_name)


driver.close()