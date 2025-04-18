import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.smoke

def test_test():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    # CHECKBOX
    lst_ckb = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

    for cb in lst_ckb:
        if cb.get_attribute("value") == "option2":
            cb.click()
            assert cb.is_selected()
            break

    time.sleep(2)