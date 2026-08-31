#Class and Object
#Lesson 1: how do classes work and how do they differ from objects?

#class here is the keyword 
#ClassName here is the name of the class
class ClassName: #class names are conventionally in the PascalCase 
    #the parameter 'self' is always a reference to the specific object being created or used
    # 'self' lets us access the object's own attributes(variables) and methods(fuctions in a class)
    def __init__(self, name, age): #special method
        self.name = name #this is an attribute the objects will have
        self.age = age
    
    def sample_method(self): #this is a method each object created can call
        print(self.name.upper()) #for now, this method will simply capitalize 

class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

#This is how you create objects from class (how to use a class)
# object_1 = ClassName(attribute_1, attribute_2)
# object_2 = ClassName(attribute_1,attribute_2)
dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

#This is how to call any methods defined in the class from each object. 
# object_1.methodname()

dog_1.bark()
dog_2.bark()

#Lesson 2: What are Methods and Attributes, and How do they work? 
# Attributes = variables that belong to an object and they hold "data". 
# Two kinds of 'attributes'
# 1. instance attributes (they are unique to each obj created from a class and usually set them with the __init__ method)
# 2. class attributes (they belong to the class itself and are shared by all instances of that class)

# Dot notation is used to access an attribute
class Dog: 
    species = "French Bulldog" #class attribute 

    def __init__(self, name): # instance attribute 
        self.name = name 
    
print(Dog.species) #French Bulldog

dog1 = Dog("Jack")
print(dog1.name) #Jack
print(dog1.species) # French Bulldog

dog2 = Dog("Tom")
print(dog2.name) #Tom
print(dog2.species) #French Bulldog  
#Note that you cannot do Dog.name because it's an instance attribute and is not shared with other methods
# However, a class instance 'species' can be accessed either way bc/ it's shared within the class. 

#Another example 
class Car:
    def __init__(self, color, model):
        self.color = color #instance attributes
        self.model = model 
    
car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.model) #Toyota Corolla
print(car_2.model) #Lamborghini Reveulto

print(car_1.color) #red
print(car_2.color) #green

# Methods = functions defined inside a class 
# Dot notation is used to access a method 

class Dog: 
    species = "French Bulldog"

    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says woof woof!"
    
jack = Dog("Jack")
jill = Dog("Jill")

print(jack.bark()) # Jack says woof woof!
print(jill.bark()) # Jill says woof woof!

#Another example 
class Car: 
    def __init__(self, color, model):
        self.color = color 
        self.model = model 
    
    def describe(self):
        return f"This is a {self.color} {self.model}" 

car1= Car("red", "Toyota Corolla")
car2= Car("green", "Lamborghini Revuelto")

print(car1.describe()) # This is a red Toyota Corolla
print(car2.describe()) # This is a green Lamborghini Revuelto 




