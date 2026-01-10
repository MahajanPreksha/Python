#Creating a class
class Students:

    #self is a default parameter and it contains the object that is being passed to the function 
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name #Class Attribute

    def get_name(self):
        return self.name

#Creating an object
student1 = Students("Preksha")
student1.set_name("Preksha")
print(student1.get_name()) #Output: Preksha
student1.marks = 100 #Instance Attribute
print(student1.marks) #Output: 100

student2 = Students("PM")
student2.set_name("PM")
print(student2.get_name()) #Output: PM