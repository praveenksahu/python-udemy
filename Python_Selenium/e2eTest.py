# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# # service_obj=Service("chromedriver-win64//chromedriver.exe")
# service_obj=Service("//Python_Selenium//chromedriver.exe")
# #service_obj=Service()
# driver =webdriver.Chrome(service=service_obj)
# driver.implicitly_wait(4)
# #driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
# products=driver.find_elements(By.XPATH,"(//div[@class='card h-100'])")
# for product in products:
#     productName=product.find_element(By.XPATH,"div/h4/a").text
#     if productName == "Blackberry":
#         product.find_element(By.XPATH,"div/button").click()
# driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
# driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
# driver.find_element(By.XPATH,"//div/div[1]/input").send_keys("India")
# wait=WebDriverWait(driver,10)
# wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
# driver.find_element(By.LINK_TEXT,"India").click()
#
# driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
# driver.find_element(By.XPATH,"//input[@type='submit']").click()
# success=driver.find_element(By.CLASS_NAME,"alert-success").text
# assert "Success" in success
#
# driver.close()