from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = False

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.geeksforgeeks.org/courses?source=google&medium=cpc&device=c&keyword=geeksforgeeks&matchtype=e&campaignid=20039445781&adgroup=147845288105&gad_source=1&gclid=EAIaIQobChMIr-SPn4zHiQMVUatmAh1dTyKvEAAYASAAEgJ_1PD_BwE")
parent_handle = driver.current_window_handle
print("Parent handle:", parent_handle)

time.sleep(3)
driver.find_element(By.XPATH, "//a[@class='link'][normalize-space()='DSA']").click()

time.sleep(3)
all_handles=driver.window_handles
print("All handles:", all_handles)

for handle in all_handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        print("Current handle:", driver.current_window_handle)

        try:
            element=driver.find_element(By.XPATH,"//a[normalize-space()='Introduction to DSA']")
            element.click()
            print("Clicked on offer section")
        except Exception as e:
            print("An error occurred:", e)

        driver.close()
driver.switch_to.window(parent_handle)
print("returned to parent window")

driver.quit()