from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

# Set up the Chrome driver
options = Options()
options.headless = False  # Set to True if you want to run in headless mode
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the website
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

try:
    # Clear a text box, send text, and get its attributes
    text_box = driver.find_element(By.ID, "user-message")
    text_box.clear()  # Clear any existing text
    text_box.send_keys("Hello, Selenium!")  # Send keys
    print("Text box displayed:", text_box.is_displayed())  # Check if displayed
    print("Text box enabled:", text_box.is_enabled())  # Check if enabled
    print("Text box tag name:", text_box.get_tag_name())  # Get tag name
    print("Text box size:", text_box.size)  # Get size
    print("Text box location:", text_box.location)  # Get location
    text_box.submit()  # Submit the form

    time.sleep(2)  # Wait for the result to be displayed

    # Get the displayed text after submission
    result_message = driver.find_element(By.ID, "display")
    print("Result message:", result_message.text)  # Get text from result

    # Example with dropdown
    dropdown = Select(driver.find_element(By.ID, "select-demo"))
    dropdown.select_by_visible_text("Monday")  # Select an option
    print("Dropdown selected:", dropdown.first_selected_option.text)  # Get selected option text

    # Checkbox interaction
    checkbox = driver.find_element(By.ID, "isAgeSelected")
    checkbox.click()  # Click checkbox
    print("Checkbox is selected:", checkbox.is_selected())  # Check if selected

    # Radio button interaction
    radio_button = driver.find_element(By.XPATH, "//input[@value='Male' and @name='optradio']")
    radio_button.click()  # Click radio button
    print("Radio button is selected:", radio_button.is_selected())  # Check if selected

    # Get CSS value of the result message
    print("Result message CSS value:", result_message.value_of_css_property("color"))  # Get CSS property

finally:
    driver.quit()
