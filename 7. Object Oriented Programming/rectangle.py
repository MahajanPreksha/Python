class Rectangle:

    def __init__(self, l, b): #Constructor
        print("Constructor has been invoked.")
        self.l = l
        self.b = b

    # def set_dimensions(self, l, b):
    #     self.l = l
    #     self.b = b
    
    def area(self):
        return self.l * self.b
    
    def perimeter(self):
        return 2 * (self.l + self.b)

l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))    
rectangle = Rectangle(l, b)
# rectangle.set_dimensions(l, b)
print("Length:", rectangle.l, "and Breadth:", rectangle.b)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())