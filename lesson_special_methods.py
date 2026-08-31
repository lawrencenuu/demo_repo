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





