class IOString():
    def __init__(self):
        self.str1=""
    def get_string(self):
        self.str1=input("Enter a string: ")
    def printstring(self):
        print("The string is:",self.str1.upper())
str1=IOString()
str1.get_string()
str1.printstring()
    

        

    