from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the Chrome driver
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=Options())
options = Options()
options.headless = False

driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

try:
    # Switch to the frame that contains the drag-and-drop elements
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

    # Locate the source (item to drag) and the target (drop area)
    source_element = driver.find_element(By.XPATH, "//img[@alt='The peaks of High Tatras']")
    target_element = driver.find_element(By.ID, "trash")

    # Perform drag-and-drop
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()

    print("Drag and drop successful.")
    time.sleep(2)  # Optional: Wait to see the result

except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the browser
    driver.quit()