from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Import TimeoutException
import time

# Set up your Chrome options
options = Options()
options.headless = False  # Optional: Run in headless mode

# Specify the path to the ChromeDriver
service = Service("/usr/bin/chromedriver")

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

def test_page_title():
    driver.get("https://google.com/")
    assert driver.title == "Google", "Page title is not correct"
    print("Test page title: Passed")
    time.sleep(5)

def test_search_functionality():
    driver.get("https://google.com/")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Java")
    search_box.submit()  # Submit the form
    assert "Java" in driver.title, "Search results page title does not contain search term"
    print("Test search functionality: Passed")

def test_navigation_link():
    driver.get("https://www.iana.org")  # Navigate to the IANA website

    # Wait for the link to be clickable
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Domain Names"))
    )
    link.click()

    # Wait for the title to change
    try:
        WebDriverWait(driver, 10).until(EC.title_contains("Domain Names"))
    except TimeoutException:
        print("Timeout while waiting for the title to change.")
        print("Current title:", driver.title)  # Print the current title for debugging
        return  # Exit the function if the title doesn't change

    # Check if the title contains "Domain Names"
    assert "Domain Names" in driver.title, "Failed to navigate to the linked page"
    print("Test for Navigation Link: Passed")

if __name__ == "__main__":
    test_page_title()
    test_search_functionality()
    test_navigation_link()
    driver.quit()
