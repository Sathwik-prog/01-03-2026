# Create class
class Employee:

    #Initializing
    def __init__(self):
        print("Employee created")

    #calling destructor
    def __del__(self):
        print("Destructor called")

def create_object():
    print("Creating Object")
    obj = Employee()
    print("Function called")
    return obj

print("Calling create_object function")
obj = create_object()
print("Program Ended")

    
   