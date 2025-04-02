import pytest

@pytest.fixture
def setup():
    print("Open Browser")
    yield
    print("Close Browser")


def test_one(setup):
    print("Login")


def test_two(setup):

    print("Update")


def test_three(setup):

    print("Logout")
