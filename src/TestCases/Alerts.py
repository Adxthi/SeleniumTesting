from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up the Chrome driver
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=Options())
options = Options()
options.headless = False
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Simple Alert - Clicks 'OK'
try:
    # Locate and click the button to trigger the alert
    driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Alert')]").click()

    # Switch to alert and accept it
    alert = driver.switch_to.alert
    print("Simple Alert Text:", alert.text)
    alert.accept()
    print("Simple Alert accepted.")
    time.sleep(2)

    # Confirmation Alert - Clicks 'Cancel'
    driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Confirm')]").click()

    # Switch to the alert, retrieve text, dismiss the alert
    alert = driver.switch_to.alert
    print("Confirmation Alert Text:", alert.text)
    alert.dismiss()  # Choose 'Cancel'
    print("Confirmation Alert dismissed.")
    time.sleep(2)

    # Prompt Alert - Enter text and click 'OK'
    driver.find_element(By.XPATH, "//button[contains(text(),'Click for JS Prompt')]").click()

    # Switch to the prompt, send text, and accept it
    alert = driver.switch_to.alert
    alert.send_keys("Selenium Test")
    alert.accept()  # Choose 'OK'
    print("Prompt Alert accepted with input.")

finally:
    # Close the browser
    driver.quit()
