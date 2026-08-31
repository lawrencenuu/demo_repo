# Lesson 3: What are special methods and what are they used for? 
# Special Methods = magic methods = dunder (double underscores) => __methodname__ 
# __init__() = this is a class initializer 

class Book: 
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    #So here is how you can define your own 
    #with these you can access the attributes and operate
    def __len__(self): 
        return self.pages

    def __str__(self): 
        return f"'{self.title}' has {self.pages} pages"
    
    def __eq__(self,other):
        return self.pages == other.pages
    
book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1))# TypeError: object of type "Book" has no len()
print(str(book1))# <__main__. Book object at 0x102ed2900> 
print(book1==book2)# False, even though they have the same number of pages 


class Cart: 
    def __init__(self):
        self.items = []

    def add(self,item): 
        self.items.append(item)

    def remove(self,item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item} is not in cart")

    def list_items(self): 
        return self.items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __contains__(self,item):
        return item in self.items
    
    def __iter__(self): 
        return iter(self.items) 
    
cart = Cart()
cart.add("Laptop")
cart.add("Wireless mouse")
cart.add("Ergo keyboard")
cart.add("Monitor")

for item in cart: # Laptop Wireless mouse Ergo keyboard Monitor
    print(item, end=" ") 

print(len(cart)) # 4
print(cart[3]) # Monitor

print('Monitor' in cart) #True
print('banana' in cart) #False 

cart.remove('Ergo keyboard') # it removes Ergo keyboard
print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana') #banana is not in cart 

#Lesson 4: How to handle object attributes dynamically? 
# 4 built-in functions to dynamically work with obj attributes 
# 1. getattr() -> access
# 2. setattr() -> create
# 3. hasattr() -> check
# 4. delattr() -> remove
# getattr(object, attribute_name, default_value)

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
person = Person("John Doe", 30)

print(getattr(person,'name')) # John Doe
print(getattr(person, 'age')) # 30 
print(getattr(person, 'city', 'Milano')) # Milano (Milano is a default value bc city doesn't exist)

attr_name = input("Enter the attribute you want to see: ")
print(getattr(person, attr_name, 'Attribute not found'))

# To look through all the attributes an object has, you can use dir() function
# it returns a list of all attribute names on the object. 
for attr in dir(person):
    #This ignores dunder methods and regular methods
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        # callable() is a built-in function
        # returns True if the obj passed to it can be called like a function or method, and False otherwise
        value = getattr(person, attr)
        print(f'{attr}: {value}')

    #Output
    # age: 30
    # name: John Doe


# To create a new attribute or update an existing one dynamically, you can use setattr() 
# setattr(object, attribute_name, value)
class Configuration: 
    pass 

settings_data = {
    'server_url' : 'https://api.example.com',
    'timeout_sec' : 30,
    'max_retries' : 5
}

config_obj = Configuration() 
# Dynamically set attributes using dictionary keys and values 
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.timeout_sec) # 30 

# To check if an attribute exists, you can use hasattr()
# hasattr(object, attribute_name)
class Product: 
    def __init__(self, name, price):
        self.name = name
        self.price = price
product_a = Product("T-Shirt", 25)

required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes: 
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missin the required attribute: '{attr}")
    else:
        #Access the attributes dynamically once their existance is confirmed 
        print(f'{attr}: {getattr(product_a,attr)}')

#output
# name: T-Shirt
# price: 25
# ERROR: Product is missin the required attribute: 'inventory_id

# To remove an attribute dynamically, you can use delattr()
# delattr(object, attribute_name)
class UserSession: 
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token #sensitive
        self.temp_counter = 0 #temporary

session = UserSession(101, 'a1b2c3d5e5')
# List of attributes to remove dynamically before "saving" the session 
attributes_to_clean = ['auth_token', 'temp_counter'] 

# Dynamically remove specified attributes 
for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')

print("\nFinal attributes remaining: ")
#Loop through the remaining attributes with dir()
for attr in dir(session):
    if not attr.startswith('__') and not callable(getattr(session, attr)):
        print(f" - {attr}: {getattr(session,attr)}")

#Output:
# Removed attribute: auth_token
# Removed attribute: temp_counter

# Final attributes remaining: 
#  - user_id: 101