from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.headless = False

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)
driver.get("https://www.geeksforgeeks.org/courses?source=google&medium=cpc&device=c&keyword=geeksforgeeks&matchtype=e&campaignid=20039445781&adgroup=147845288105&gad_source=1&gclid=EAIaIQobChMIr-SPn4zHiQMVUatmAh1dTyKvEAAYASAAEgJ_1PD_BwE")

print("Page title is:", driver.title)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )

finally:
    driver.close()