from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.headless = False

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)
driver.get("https://www.geeksforgeeks.org/courses?source=google&medium=cpc&device=c&keyword=geeksforgeeks&matchtype=e&campaignid=20039445781&adgroup=147845288105&gad_source=1&gclid=EAIaIQobChMIr-SPn4zHiQMVUatmAh1dTyKvEAAYASAAEgJ_1PD_BwE")

print("Page title is:", driver.title)

driver.find_element(By.XPATH, "//a[@class='link'][normalize-space()='DSA']").click()
print("Page title is:", driver.title)
driver.close()