class Parent:

    def __init__(self):
        self.super_attribute = True
        print("This is the parent class.")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is a child class.")
        print(self.super_attribute)

child1 = Child()

'''Output:
This is the parent class.
This is a child class.
True
'''