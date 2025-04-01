import time

from AppData.Local.Programs.Python.Python312.Lib.test.test_copy import equality_comparisons
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(10)
#actual string
expectedStr=["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
result=driver.find_elements(By.XPATH,"//div[@class='products']/div")
#print(len(result))
actualStr=[]
for res in result:

    actualStr.append(res.find_element(By.XPATH,"h4").text)

    res.find_element(By.XPATH,"div/button").click()
print(f"Expexted List : {expectedStr}")
print(f"Actual List : {actualStr}")
assert expectedStr == actualStr
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
prices=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
summ=0
for price in prices:
    summ=summ + int(price.text)
print(summ)

summa= int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert summ == summa

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
time.sleep(10)
discount_price= float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
assert discount_price < summa
print(discount_price)

#driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
#time.sleep(2)