from main import helloworld
from main import add

def test_helloworld():
    helloworld()

def test_add():
    assert add(1, 5) == 6
