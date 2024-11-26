from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up the Chrome driver
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=Options())
options = Options()
options.headless = False
driver.get("https://google.com/")

title=driver.title
l=len(title)
print("Title is:",title,"and length is:",l)

url=driver.current_url
print(url)

if url=="https://www.google.com/":
    print("URL is correct")
else:
    print("URL is incorrect")

ps=driver.page_source
lps=len(ps)
print("length of page source is:",lps)

driver.close()