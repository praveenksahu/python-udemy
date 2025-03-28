from selenium import webdriver
#from selenium.webdriver.ie.service import Service
from selenium.webdriver.firefox.service import Service
#driver = webdriver.Edge()
# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/angularpractice/")
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)

#service_obj= Service("C:/Python_Selenium/PythonUdemyPrj/Python_Selenium/geckodriver.exe")
driver=webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/angularpractice/")