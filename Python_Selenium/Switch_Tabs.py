from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.service import Service
driver=webdriver.Firefox()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsOpened = driver.window_handles

#Switched to New Window
driver.switch_to.window(windowsOpened[1])
print (driver.find_element(By.TAG_NAME,"h3").text)
#driver.close()
#Switched to Previous Window
driver.switch_to.window(windowsOpened[0])
print (driver.find_element(By.TAG_NAME,"h3").text)
#driver.close()