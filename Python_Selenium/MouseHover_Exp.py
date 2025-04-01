import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)

action=ActionChains(driver)
#MouseHover
action.move_to_element(driver.find_element(By.XPATH,"//button[@id='mousehover']")).perform()

#Right Click
action.context_click(driver.find_element(By.CSS_SELECTOR,"a[href='#top']")).perform()

#Click on MouseHover options
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()