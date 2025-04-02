
def test_1():
    x=10
    y=10
    assert x == y, "Both Variables are not Equal"

def test_2():
    str="Selenium"
    str2="This is the world of Selenium"

    assert str in str2, "String not exist"