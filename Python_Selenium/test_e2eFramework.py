import json
import os.path
import sys

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pageObjects.login import LoginPage

test_data_path = '../data/test_e2eFramework.json'
with open(test_data_path) as f:
    test_data=json.load(f)
    test_list=test_data["data"]
#@pytest.mark.smoke
@pytest.mark.parametrize("test_list_items",test_list)
def test_e2e(browserInstance,test_list_items):
    driver = browserInstance
    login_page=LoginPage(driver)
    print(login_page.getTitle())
    shop_page = login_page.login(test_list_items["userEmail"], test_list_items["userPassword"])
    shop_page.add_product_to_cart(test_list_items["productName"])
    print(shop_page.getTitle())
    checkout_confirmation=shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_orders()





