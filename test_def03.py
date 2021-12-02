try:
    from def03 import main 
except ImportError:
    assert False, "Not found"
    # def01 = lambda: None
#Create test to check import def01

#Create a test function to test the def01 function
def test_main():
    assert type(main()) == float, "Not a float"