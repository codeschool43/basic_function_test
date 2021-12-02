
try:
    from def08 import main 
except ImportError:
    assert False, "Not found"
    
#Create a test to check if main is returning 'Hello World'
def test_main():
    #Assign the return value of main to a variable
    output = main()
    #Assign Pi ton 4 decimal places to expected
    expected = 3.1415
    #Check if the output is equal to the expected
    assert output == expected,'Wrong answer'