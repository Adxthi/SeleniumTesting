from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# Set up the Chrome driver
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=Options())
options = Options()
options.headless = False
# Launch Website
driver.get("https://www.lambdatest.com/selenium-playground/select-dropdown-demo")

try:
    # Wait until the dropdown is available
    dropdown_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "select-demo"))
    )
    # Using Select class for selecting value from dropdown
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Wednesday")
    print("Dropdown selection successful.")
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the Browser
    driver.quit()
