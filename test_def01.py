try:
    from def01 import def01
except ImportError:
    assert False, "Not found"


def test_def01():
    assert def01() == 0, "def01 is not 0"