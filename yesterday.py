# Create Dog class
class Dog:
    # Class variable
    animal = "Dog"

    # Constructor with instance variables
    def _init_(self, breed, colour):   
        self.breed = breed
        self.color = colour           

# Create two objects
dog1 = Dog("Labrador", "Black")
dog2 = Dog("Beagle", "Brown")

# Display details
print("Dog 1 Details:")
print("Animal:", dog1.animal)
print("Breed:", dog1.breed)
print("Colour:", dog1.colour)         

print("\nDog 2 Details:")
print("Animal:", Dog.animal)
print("Breed:", dog2.breed)
print("Colour:", dog2.colour)         