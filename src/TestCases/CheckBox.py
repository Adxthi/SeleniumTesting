from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
service = Service("/usr/bin/chromedriver")  # Update to your ChromeDriver path
options = Options()
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to the DemoQA Checkbox page
    driver.get("https://demoqa.com/checkbox")

    # Wait until the checkbox element is visible
    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='tree-node-home']")))

    # Check if the checkbox is selected before clicking
    print("Is checkbox selected? (Before clicking):", checkbox.is_selected())

    # Click the checkbox to select it
    checkbox.click()

    # Confirm if the checkbox is selected after clicking
    print("Is checkbox selected? (After clicking):", checkbox.is_selected())

finally:
    # Close the browser
    driver.quit()
