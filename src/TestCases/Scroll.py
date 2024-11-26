from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Set up the Chrome driver
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=Options())
options = Options()
options.headless = False
driver.get("https://www.javatpoint.com/")

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("scrolled to bottom")
# Scroll to the top of the page
driver.execute_script("window.scrollTo(0, 0);")
print("scrolled to top")

driver.close()
