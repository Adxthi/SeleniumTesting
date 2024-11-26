from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set Chrome options
options = Options()
options.headless = True  # Run Chrome in headless mode

# Specify the path to ChromeDriver in the Service object
service = Service("/usr/bin/chromedriver")

# Initialize Chrome WebDriver with options and service
driver = webdriver.Chrome(service=service, options=options)

# Open the website and print the title
driver.get("https://google.com/")
print(driver.title)

# Close the browser
driver.quit()
