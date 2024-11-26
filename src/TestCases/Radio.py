from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up the Chrome driver
options = Options()
options.headless = False  # Set to True if you want to run in headless mode
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# Open the HTML file in the browser
driver.get("file:///home/dell/Documents/HTML/radio_buttons.html")  # Update the path accordingly

try:
    # Wait for the page to load
    time.sleep(2)

    # Select a radio button (e.g., Banana)
    banana_radio = driver.find_element(By.XPATH, "//input[@value='Banana']")
    banana_radio.click()  # Click the radio button

    # Verify if the radio button is selected
    print("Is Banana selected?", banana_radio.is_selected())  # Should return True

    # Click the submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # Wait to see the result
    time.sleep(2)

    # Get and print the result text
    result_text = driver.find_element(By.ID, "result")
    print("Result text:", result_text.text)

finally:
    # Close the browser
    driver.quit()
