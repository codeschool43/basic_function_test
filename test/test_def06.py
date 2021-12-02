try:
    from def06 import main 
except ImportError:
    assert False, "Not found"
    
#Create a test to check if main is returning 'Hello World'
def test_main():
    assert main() == "Hello World", "Not Hello World"