try:
    from def02 import main 
except ImportError:
    assert False, "Not found"
    # def01 = lambda: None
#Create test to check import def01

#Create a test function to test the def01 function
def test_def01():
    assert type(main()) == int, "Not an integer"