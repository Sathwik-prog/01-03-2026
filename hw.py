class Circle:
    
    def _init_(self, radius):      
        self.radius = radius
    
    def area(self):
        pi = 3.14
        area = pi * self.radius ^ 2    
        return area
    
    def perimeter(self):
        pi = 3.14
        perimeter = 2 * pi * radius    
        return perimeter


c1 = Circle(5)

print("Area of circle:", c1.area())
print("Perimeter of circle:", c1.perimeter())