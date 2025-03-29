import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("chromedriver-win64//chromedriver.exe")

driver =webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
#print(len(countries))
for country in countries:
    if country.text=="India":
        country.click()
        break
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"

time.sleep(2)