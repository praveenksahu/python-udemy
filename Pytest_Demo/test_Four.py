#Inbuild markers Example
import pytest
import sys

@pytest.mark.skip
def test_signIn():
    print("Provide User Name and Password")

@pytest.mark.skipif(sys.version_info>(1,10),reason="Python Version not Supported")
def test_welCome():
    print("Welcome to our Portal")

@pytest.mark.xfail
def test_addProduct():
    assert False
    print("Logout successfully")

def test_closeApp():
    assert True
    print("Product Added Successfully")


