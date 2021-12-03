# Create function to find Pi to 4 number of decimal places.
def main():
    """
    Calculate Pi to n number of decimal places.
    """
    #Calculate Pi to n number of decimal places.
    n = 4
    #Create variable to store Pi.
    pi = 3.1415926535897931159979634685441852
    #Return Pi to n number of decimal places.
    answer = int(pi*10000)/10000
    return answer

print(main())