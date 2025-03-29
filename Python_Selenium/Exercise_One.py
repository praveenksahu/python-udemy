import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# #CHECKBOX
# lst_ckb=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
#
# for cb in lst_ckb:
#     if cb.get_attribute("value") == "option2":
#         cb.click()
#         assert cb.is_selected()
#         break

#RADIO
rad_btn=driver.find_elements(By.XPATH,"//input[@type='radio']")
for rb in rad_btn:
    if rb.get_attribute("value") == "radio2":
        rb.click()
        assert rb.is_selected()
        break
time.sleep(2)