import pytest

@pytest.mark.smoke
def test_login():
    print("Welcome to Login Page")

@pytest.mark.regression
def test_additems():
    print("Items added successfully")

@pytest.mark.smoke
def test_logout():
    print("You logged out Successfully")