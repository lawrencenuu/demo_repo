# 1
numbers = []

for x in range(5):
    numbers.append(x)
# ==>
numbers = [x for x in range(5)]

# 2
squares = []

for x in range(5):
    squares.append(x * x)

#==> 
square =[x*x for x in range(5)]

# 3
even = []

for x in range(10):
    if x % 2 == 0:
        even.append(x)
#==> 
even=[x for x in range(10) if x%2==0]

# 4
letters = []
text = input()
for char in text:
    if char.isalpha():
        letters.append(char.lower())
# ==> 
letters = [char.lower() for char in text if char.isalpha()]

#[WHAT_TO_KEEP_OR_CREATE for ITEM in COLLECTION if CONDITION]

numbers = [num * 2 for num in range(10)]

numbers = [num for num in range(20) if num % 2 == 0]

numbers = [num * 3 for num in range(20) if num % 2 != 0]

letters = [char.lower() for char in "Hello World" if char.isalpha()]

fruits = ["apple", "banana", "cat", "elephant"]
words = [word.upper() for word in fruits if len(word) > 4] 

result = [str(num) for num in range(1, 30) if num % 3 == 0]

names = [name.lower() for name in ["Alice", "Bob", "Charlie"]]

numbers = [num for num in range(1, 21) if num > 10]

words = [word.lower() for word in ["Python", "Java", "C++", "JavaScript"] if len(word) >= 5]

squares = [num ** 2 for num in range(1, 11)]

short_words = [word for word in ["cat", "elephant", "dog", "butterfly", "ant"] if len(word) <= 3]

result = [num ** 2 for num in range(1, 16) if num % 2 == 0]

characters = [char.upper() for char in "Hello123World!" if char.isalpha()]

