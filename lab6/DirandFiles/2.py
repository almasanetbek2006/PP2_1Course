import os

def checking(a):
    # Check existence
    if os.path.exists(a):
        print(f"the path '{a}' exists")
    else:
        print(f"the path '{a}' does not exist")
        return  
    
    # Check readability
    if os.access(a, os.R_OK):
        print(f"the path '{a}' is readable")
    else:
        print(f"the path '{a}' is not readable")
    
    # Check writability
    if os.access(a, os.W_OK):
        print(f"the path '{a}' is writable")
    else:
        print(f"the path '{a}' is not writable")
    


a = input("Enter the path to check: ")
checking(a)