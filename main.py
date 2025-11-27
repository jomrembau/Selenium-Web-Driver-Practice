from os import times

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li time")
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

all_events = {}

times_list = [x.text for x in times]
events_list = [x.text for x in events]

for x in range(0,len(times_list)):
    all_events[x] = {
        "time": times_list[x],
        "name": events_list[x]
    }

print(all_events)

driver.quit()