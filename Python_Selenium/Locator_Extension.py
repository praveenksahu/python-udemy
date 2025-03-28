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
driver.maximize_window()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

time.sleep(2)