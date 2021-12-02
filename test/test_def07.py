try:
    from def06 import main 
except ImportError:
    assert False, "Not found"
    
#Create a test to check if main is returning 'codeschooluz'
def test_main():
    assert main() == "codeschooluz", "Wrong answer"