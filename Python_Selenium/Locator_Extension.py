import time

from selenium import webdriver
#Chrome Driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("chromedriver-win64//chromedriver.exe")

#C:\Users\aarya\Downloads\chromedriver-win64.zip\chromedriver-win64

driver =webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/")

driver.find_element(By.LINK_TEXT,"Forgot password?").click()


time.sleep(2)