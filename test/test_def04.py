try:
    from def04 import main 
except ImportError:
    assert False, "Not found"
#Create a test check if main is returning a string
def test_main():
    assert type(main()) == str, "Not a string"