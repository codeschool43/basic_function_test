try:
    from def05 import main 
except ImportError:
    assert False, "Not found"
#Create a test check if main is returning a boolean.
def test_main():
    assert type(main()) == bool, "Not a bool"