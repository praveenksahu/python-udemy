import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("VishalM")
driver.find_element(By.NAME,"email").send_keys("abc@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR," #inlineRadio1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Hello")

assert "Success" in message

time.sleep(2)
#driver.find_element(By.ID,"exampleFormControlSelect1")