import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
message = driver.find_element(By.CSS_SELECTOR,".red").text
# Regular expression pattern for matching email addresses
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# Find all email addresses in the given text
email_address = re.findall(email_pattern, message)
#print(email_address)
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID,"username").send_keys(email_address[0])
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Test@123")
driver.find_element(By.ID,"signInBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

time.sleep(2)