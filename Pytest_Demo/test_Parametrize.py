import pytest
from AppData.Local.Programs.Python.Python312.Lib.platform import uname


@pytest.mark.parametrize("Uname, Passwd",
                         [
                             ("Test_Uname","Test_Passwd"),
                             ("stage_Uname","stage_Passwd"),
                             ("prod_Uname","prod_Passwd")
                         ])
def test_parametrize(Uname,Passwd):
    print(Uname)
    print(Passwd)
