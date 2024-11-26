from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the browser
browser = webdriver.Chrome()

# Define the number of times to repeat the process and the phone number
frq = 10
mob = "1234567890"

for i in range(frq):
    browser.get("https://www.flipkart.com/account/login?ret=/")

    # Locate the mobile number input field and enter the mobile number
    number = browser.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
    number.send_keys(mob)
    print(browser.title)



    time.sleep(2)  # Wait a moment before the next iteration

# Close the browser
browser.quit()
