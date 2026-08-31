# numbers = [1, 2, 3, 4, 5]
# numbers.append(8) 
# print(numbers)

# even_numbers = [2,4,6,8]
# numbers.extend(even_numbers)
# print(numbers)

# numbers.insert(0, 10) 
# print(numbers)

# numbers.remove(10)
# print(numbers)

# print(numbers.pop(3))
# print(numbers)
# numbers.sort()
# print(numbers)
# # numbers.clear()
# # print(numbers)

# numbers.reverse()
# print(numbers)

# # numbers.index(3)
# print(numbers.index(3))

# # developer = 'Jessica' 
# # print(tuple(developer))
# developer = ('Alice', 34, 'Rust Developer')
# name, age, job = developer
# print(name)
# print(age)
# print(job)


# programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
# print(programming_languages.count('Rust'))

# programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
# sorted_languages =sorted(programming_languages, key = len, reverse=True) 

# for language in sorted_languages: 
#     print(language)
   
# print('\n')
# text = 'I love programming'
# split_text = text.split()
# for char in split_text: 
#     print(char)

# categories = ['Fruit', 'Vegetable']
# foods = ['Apple', 'Carrot', 'Banana']

# for category in categories: 
#     for food in foods: 
#         print(f'{category}: {food}')


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# products = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in numbers: 
#     for product in products: 
#         print( f'{number} x {product} = {number * product}')
    
#     print('\n')

# dice_1  = [1, 2, 3, 4, 5, 6]
# dice_2 = [1, 2, 3, 4, 5, 6]

# for d1 in dice_1:
#     for d2 in dice_2: 
#         print(f'({d1}, {d2})', end = " ")
    
#     print()

# secret_number = 7 
# guess = 0 

# while guess != secret_number: 
#     guess = int (input("Guess the secret number between 1 and 10: "))
#     if guess< secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")

# print("Congratulations! You guessed the secret number.")

# developer_names = ['Jess', 'Naomi', 'Tom', 'Alice', 'Bob', 'Charlie']

# for developer in developer_names:
#     if developer == 'Tom':
#         continue
#     print(developer, end=" ")

# words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

# for word in words:
#     print(f"The word {word} contains:", end=" ")

#     found = False

#     for vowel in "aeiou":
#         if vowel in word:
#             print(vowel, end=" ")
#             found = True

#     if not found:
#         print("no vowels", end="")

#     print()


# for num in range(100,1,-5):
#     print(num, end=" ")

# languages = ['Spanish', 'English', 'Russian', 'Chinese']
# print(list(enumerate(languages)))

# languages = ['Spanish', 'English', 'Russian', 'Chinese']

# for index, language in enumerate(languages, 1):
#     print(f'Index {index} and language {language}')

# developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
# ids = [1, 2, 3, 4]

# print(list(zip(developers, ids)))

# developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
# ids = [1, 2, 3, 4]

# for name, dev_id in zip(developers, ids):
#     print(f'Name: {name}', end=", ")
#     print(f'ID: {dev_id}')

# number = int(input("Enter a number to create a list: "))
# num_list = []

# for num in range (number):
#     if num % 2 == 0 and num != 0:
#         num_list.append(num)

# print(num_list)

# even_num_list = [num for num in range (1, 100) if num%2==0]
# print(even_num_list)

# numbers = [1, 2, 3, 4, 5]
# result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
# print(result)

# words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

# def is_long_word(word):
#     return len(word) > 4
# long_words = list(filter(is_long_word, words))


# long_words = list(filter(lambda word: len(word) > 4, words))
# print(long_words)

# celsius = [0, 10, 20, 30, 40]

# def to_fahrenheit(temp):
#     return (temp * 9/5) + 32

# fahrenheit = list(map(to_fahrenheit, celsius))
# print(fahrenheit)

# Lambda Functions
# numbers = [1, 2, 3, 4, 5]
# even_numbers = list(filter(lambda x: x%2 ==0, range(1, 20)))
# print(even_numbers)

# def pin_extractor(poems):
#     secret_codes = []
#     for poem in poems:
#         secret_code = ''
#         lines = poem.split('\n')
#         for line_index, line in enumerate(lines):
#             words = line.split()
#             if len(words) > line_index:
#                 secret_code += str(len(words[line_index]))
#             else:
#                 secret_code += '0'
#         secret_codes.append(secret_code)
#     return secret_codes        

# poem = """Stars and the moon
# shine in the sky
# white and
# until the end of the night"""

# poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
# poem3 = 'There\nonce\nwas\na\ndragon'

# print(pin_extractor([poem, poem2, poem3]))

#Lab
# Number Pattern
# def number_pattern(n):
#     pattern =""
#     if not isinstance(n,int):
#         return "Argument must be an integer value."
#     elif n < 1: 
#         return "Argument must be an integer greater than 0."

#     for i in range(1,n+1): 
#         pattern += str(i) + " "

#     return pattern.rstrip()

# print(number_pattern(4))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# # result = [num for num in numbers if num%2==0]
# result1 = list(filter(lambda x: x%2==0, numbers))
# # for num in numbers: 
# #     if num%2 == 0: 
# #         result.append(num)

# print(result1)

# def sleep_in(weekday, vacation):
#   return not weekday or vacation

# def diff21(n): 
#     return 21-n if n<=21 else (n-21)*2

# print(diff21(31))  # Output: 2

# def front_back(str):
#   if len(str) <=1:
#     return str
#   elif len(str) == 2:
#     front = str[0]
#     back = str[-1]
#     return back + front
#   else:
#     front = str[0]
#     back = str[-1]
#     return back + str[1:-1] + front

# print(front_back(""))  # Output: "eodc"

# def string_splosion(str):
#   text = ''
#   for i in range(len(str)):
#     text += str[:i+1]
#   return text

# def array123(nums):
#   seq = [1,2,3]
#   for i in range(len(nums)-2):
#     if nums[i:i+3] == seq:
#       return True
#   return False

# print(array123([1, 1, 2, 3, 1]))  

# def string_match(a, b):
#     count = 0
#     for i in range(len(a)-1):
#         for j in range(len(b)-1):
#             if b[j]+b[j+1] == a[i]+a[i+1] and i==j:
#                 count += 1
#     return count

# print(string_match('xxcaazz', 'xxbaaz')) 
# print(string_match('aabbccdd', 'abbbxxd')) 

# def make_tags(tag, word):
#   return f'<{tag}>{word}</{tag}>'

# print(make_tags('i', 'Hello'))  # Output: "<i>Hello</i>"

# def make_out_word(out, word):
#   return out.replace(out[2:4],word)

# print(make_out_word('<<>>', 'Yay'))  # Output: "<<Yay>>"

# def rotate_left3(nums):
#   first, *rest = nums
#   rest.append(first)
#   return rest

# print(rotate_left3([1, 2, 3]))  # Output: [2, 3, 1]

# def max_end3(nums):
#   biggest = 0
#   new_nums = []
#   for i in range(len(nums)):
#     if i+1 < len(nums)-1 and nums[i] <= nums[i+1]:
#       biggest = nums[i+1]
#     elif i < len(nums)-1 and nums[i] > biggest:
#       biggest = nums[i]

#   for i in range(len(nums)):
#     new_nums.append(biggest)
    
#   return new_nums

# print(max_end3([1, 2, 3]))  # Output: [3, 3, 3]
# print(max_end3([11, 5, 9]))  # Output: [11, 11, 11]

# numbers = str(input())
# number_list= list(map(int, str(numbers).split()))
# number_list.sort()
# print(number_list[1])

# numbers = input("Enter a list of numbers separated by spaces: ")
# number_list = list(map(int, numbers.split()))
# number_list.sort()
# print(number_list[1])

# string1 = input()
# string2 = input()
# if len(string1)<len(string2):
#   if string1 in string2:
#     text = string2.replace(string1,"")
#     print(text)
#   else: 
#     print(string2) 
# else: 
#   if string2 in string1:
#     text = string1.replace(string2,"")
#     print(text)
#   else:
#     print(string1)

# num = int(input())

# def factorial(n):
#   total = 1
#   if n <= 20: 
#     for i in range(n):
#       total *= n
#       n -= 1 
      
#   return total

# print(factorial(num))

# num = int(input())
# for i in range(num):
#   for j in range(num):
#     print("*", end="")
#   print()

# from math import sqrt


# num = int(input())
# if num > 1:
#     exist = False
#     for i in range(int(sqrt(num))): 
#         if num % (i+1) == 0 and not (i+1) == 1 :
#             exist = True
#             break
#     if exist:
#         print("No")
#     else:
#         print("Yes")
# else:
#     print("No")

# text = str(input())
# lst = text.split()
# num1 = int(lst[0])
# num2 = int(lst[1])
# for i in range(num1):
#   for j in range(num2):
#     print("*", end="")
#   print()

# num = int(input())

# def Fibo(n):
#     if n == 1:
#         return "0"

#     lst = [0, 1]

#     for i in range(n - 2):
#         next_num = lst[-1] + lst[-2]
#         lst.append(next_num)

#     return ' '.join(map(str, lst))

# print(Fibo(num))

# 0 1 1 2 3 5 8 13 21 34 55 89 144
# input_str = str(input())
# input_list = input_str.split()
# num1, num2 = int(input_list[0]), int(input_list[1])
# for i in range(num1): 
#   for j in range(num2):
#     if i == 0 or i== num1-1 or j==0 or j==num2-1:
#       print("*", end="")
#     else:
#       print("-", end="")
#   print()

# num1 = int(input())
# num2 = int(input())
# check = False 

# for i in range(1,num1+1):
#     if not (i == num2 or i == num2-1 or i == num2+1):
#         print(i, end=" ")
#         check = True

# if not check:
#     print("DIE")

# name = str(input())

# def greeting(n):
#   greet = "Hello, " + n + "."
#   return greet

# print(greeting(name))

# num = int(input())
# years = 0
# days = 0
# if num>0: 
#     years += num//(60*24*365)
#     days += ((num/(60*24*365)) - years) * 365

# print(years, int(days))

# Input is very important so no .strip() is used and the input must follow
# the exact "Monday", "Tuesday",... where the first char is capitalized 
# text = input().strip().lower()
# if len(text)< 6 or len(text) > 1000:
# 	print("Input is invalid")
      
# elif text.lower() == "monday":
#     print("Fortune : Purple")
#     print("Unfortunate : Red")
      
# elif text.lower() == "tuesday":
#     print("Fortune : Orange")
#     print("Unfortunate : Yellow, White")

# elif text.lower() == "wednesday":
#     print("Fortune : Black, Brown, Gray")
#     print("Unfortunate : Pink")

# elif text.lower() == "thursday":
#     print("Fortune : Red")
#     print("Unfortunate : Purple")

# elif text.lower() == "friday":
#     print("Fortune : Pink")
#     print("Unfortunate : Black, Blue, Gray")

# elif text.lower() == "saturday":
#     print("Fortune : Blue, Baby Blue")
#     print("Unfortunate : Green")

# elif text.lower() == "sunday":
#     print("Fortune : Green")
#     print("Unfortunate : Blue, Baby Blue")
# else:
#     print("Input is invalid")


# num = int(input())
# for i in range(num):
#     for j in range(i+1):
#         print("*",end="")
#     print()
  
# This piece of code is not working for all test cases. 
# text = str(input()).lower()
# def table(n):
#     alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
#     char_num = []
#     for i in n:
        
#         for char, num in zip(alphabet,nums):
#             if char == i:
#                 char_num.append(num)
#     return char_num
# lst_num = list(table(text))
# total = 0
# for i in range(len(lst_num)):
#     if lst_num[i]==' ' or lst_num[i]=="!":
#         total +=0
#     else:
#         total += (lst_num[i]-i)

# print(total)

# text = input().lower()

# alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
#             'n','o','p','q','r','s','t','u','v','w','x','y','z']

# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,
#         14,15,16,17,18,19,20,21,22,23,24,25,26]

# total = 0
# index = 0

# for letter in text:
#     if letter in alphabet:
#         for char, num in zip(alphabet, nums):
#             if letter == char:
#                 total += num - index
#                 break

#     index += 1

# print(total)

# def love6(a, b):
#   if a==6 or b==6:
#     return True
#   elif (abs(a)+(abs(b))) == 6:
#     return True
#   else:
#     return False

# def in1to10(n, outside_mode):
#     if not outside_mode:
#         if n>=1 and n <=10:
#             return True
#         else:
#             return False
#     else:
#         if n<=1 or n >=10:
#             return True
#         else:
#             return False

# def make_bricks(small, big, goal):
#   small_bricks = small*1
#   big_bricks = big*5
  
#   if big_bricks == goal:
#     return True
#   elif big_bricks < goal:
#     if (big_bricks + small_bricks) >= goal:
#       return True
#     else: 
#       return False 
#   else: 
#     n = 5
#     for i in range(big):
#       if n<= (goal-5):
#         n += 5
#     if n+small_bricks >= goal:
#       return True
#     else:
#       return False
    
# #Better Version
# def make_bricks(small, big, goal):
#     big_needed = min(big, goal // 5)
#     remaining = goal - (big_needed * 5)

#     return remaining <= small

# print(make_bricks(3, 2, 8)) #True
# print(make_bricks(3, 1, 9)) #False
# print(make_bricks(0, 3, 10)) 
# print(make_bricks(2, 1000000, 100003))

# def lone_sum(a, b, c):
#   if a==b==c:
#     return 0
#   elif a==b:
#     return c
#   elif b==c:
#     return a
#   elif c==a:
#     return b
#   else:
#     return a+b+c
  
# print(lone_sum(2,2,2))
# print(lone_sum(1, 2, 3) )
# print(lone_sum(3, 2, 3) )
# print(lone_sum(3, 3, 3)) 

# text = str(input()).strip().lower() 
# char = str(input())
# times = 0
# ind = []
# for index, i in enumerate(text): 
#   if i==char: 
#     times += 1
#     ind.append(str(index))

# places = ', '.join(ind)
# if times == 0:
#   print("ERROR") 
# else: 
#   print(times)
#   print(places)


# num1 = int(input())
# num2 = int(input())
# if num1>num2: 
#   container = []
#   for i in range(num1,num2-1,-1):
#      for j in range(num1,i-1,-1):
#         container.append(str(j))
#   result = " ".join(container)
#   print(result)
# elif num2>num1: 
#     container = []
#     for i in range(num2,num1-1,-1):
#         for j in range(num2,i-1,-1):
#             container.append(str(j))
#     result = " ".join(container)
#     print(result)
# else: 
#   print(num1)

#Experiment 
# num1 = 4
# num2 = 0
# for i in range(num1,num2,-1):
#     for j in range(num1,i-1,-1):
#         print(j, end=", ")
# 4, 4, 3, 4, 3, 2, 4, 3, 2, 1


# num = int(input())
# for i in range(num):
#   for j in range(num,i,-1):
#     print("*",end="")
#   print()

# num= int(input())
# rounded_num= round(num,-1)
# print(rounded_num)

# def make_chocolate(small, big, goal):
#     required_chocolate = min(big,goal//5)
#     remaining = goal-(required_chocolate*5)

#     if remaining <= small:
#         return remaining
#     else:
#         return -1
# print(make_chocolate(4, 1, 9))
# print(make_chocolate(6, 2, 7))
# print(make_chocolate(4, 1, 10))

#partially working experiment 
# def make_chocolate(small, big, goal):
#   sm = small*1
#   bg = big*5
#   if bg+sm < goal:
#     return -1
#   elif bg<=goal or bg+sm ==goal:
#     check=0
#     for i in range(goal-bg):
#       check += 1
#     return check
#   elif bg>goal:
#     num = bg//5
#     if num <
#     check=0
#     for i in range(goal):
#       check+=1
#     return check

#calculator problem 
# num1 = int(input())
# symbol = str(input())
# num2 = int(input())
# if symbol=='*':
#     print(num1 * num2)
# elif symbol=='+':
#     print(num1+num2)
# elif symbol=='-':
#     print(num1-num2)
# elif symbol=='/':
#        if num2 !=0:
#             print(int(num1/num2))
#        else:
#             print("error")
# elif symbol=='%':
#       if num2!=0:
#             print(num1%num2)
#       else:
#             print("error")
# else:
#     print("error")

# def count_hi(str):
#     count = 0
#     modified = str.lower()
#     text =[]
#     for i, char in enumerate(modified):
#            text.append(char)
    
#     for i in range(len(text)):
#           if text[i] =='h' and text[i+1] =='i':
#                 count+=1
#     return count

# print(count_hi('Hiworld'))
# print(count_hi('ABChi hi'))

# def xyz_there(str):
#   check = False
#   for i in range(len(str)-2):
#     if str[i:i+3]=='xyz':
#       if i == 0 or str[i-1] != '.':
#         check = True
#   return check


# import sys
# import math

# data = list(map(int, sys.stdin.read().split()))
# print('Input data:', data)

# num = data[0]
# scores = data[1:num+1]
# num = int(input()) 
# scores = str(input()).split(" ") 
# lst_scores = [] 
# for i in scores: 
#     lst_scores.append(int(i))

# sorted_scores = sorted(scores)
# print(sorted_scores)
# percentiles = [10, 30, 50, 70, 90]
# percentile_scores = []

# for k in percentiles:
#     p = k * (num + 1) / 100
#     position = math.ceil(p)
#     percentile_scores.append(sorted_scores[position - 1])

# p10, p30, p50, p70, p90 = percentile_scores

# result = []

# for score in scores:
#     if score >= p90:
#         result.append("A")
#     elif score >= p70:
#         result.append("B")
#     elif score >= p50:
#         result.append("C")
#     elif score >= p30:
#         result.append("D")
#     elif score >= p10:
#         result.append("E")
#     else:
#         result.append("F")

# print(" ".join(result))
       
    
# import sys
# import math 

# data = list(map(int,sys.stdin.read().split()))
# num = data[0]
# scores=data[1:num+1] 
# sorted_scores = sorted(scores) 
  
# percentiles = [10,30,50,70,90] 
# percentile_scores = []

# for k in percentiles: 
# 	p = k*(num+1)/100
# 	position = math.ceil(p) 
# 	percentile_scores.append(sorted_scores[position-1])
      
# P10, P30, P50, P70, P90 = percentile_scores
# result = []

# for score in scores: 
# 	if score >=P90: 
# 		result.append("A") 
# 	elif score >=P70:
# 		result.append("B")
# 	elif score >= P50:
# 		result.append("C") 
# 	elif score >= P30: 
# 		result.append("D") 
# 	elif score >= P10: 
# 		result.append("E") 
# 	else: 
# 		result.append("F")
          
# print(" ".join(result))


# data = 'Tutorism is Everywhere'
# num = 3
# data = 'VueJS is da best'
# num = 4
# data = str(input())
# num = int(input())

# for i in range(len(data)): 
#     if i%num == 0: 
#         print(data[i], end="")

# ----*
# ---**
# --***
# -****
# *****
# num = 5
# for i in range(num):
#     for j in range(num-1,i,-1):
#         print("-",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()

# *****
# -****
# --***
# ---**
# ----*
# num = 5
# for i in range(num):
#     for j in range(i):
#         print("-",end="")
#     for j in range(num):
#         if i<=j:
#             print("*",end="")
#     print()

#Filled diamond
# input = 3
# --*--
# -***-
# *****
# -***-
# --*--
# num = int(input())
# size = num * 2 - 1
# center = size // 2
# for i in range(size):
#     for j in range(size):
#         if abs(i - center) + abs(j - center) <= center:
#             print("*", end="")
#         else:
#             print("-", end="")
#     print()

#Input 9
# *********
# **-----**
# *-*---*-*
# *--*-*--*
# *---*---*
# *--*-*--*
# *-*---*-*
# **-----**
# *********
# num = int(input())
# for i in range(num):
#     for j in range(num): 
#         if i==0 or j ==0 or i==num-1 or j == num-1 or i==j or i+j == num-1:
#             print("*",end="")
#         else: 
#             print("-", end="")
#     print()
# import math

# num1 = int(input())
# num2 = int(input())

# start = min(num1, num2)
# end = max(num1, num2)

# total = 0

# for i in range(start, end):
#     if i < 2:
#         continue

#     is_prime = True

#     for j in range(2, int(math.sqrt(i)) + 1):
#         if i % j == 0:
#             is_prime = False
#             break

#     if is_prime:
#         total += i

# print(total)

#SUM OF PRIME
# num1 = int(input())
# num2 = int(input())
# start = min(num1, num2)
# end = max(num1,num2) 
# total =0
# for i in range(start,end): 
#     if i == 2:
#         total += i
#     else: 
       
#         is_Prime = True
        
#         for j in range(2,i//2+1):
#             if i%j==0:
#                 is_Prime = False
#                 break
#         if is_Prime: 
#             total +=i
# print(total)

#KMUTT LOGO Dots
# num = int(input()) 
# size = num*3+1
# for i in range(size):
#     for j in range(size):
#         if (i==num or j==num) and (i < size-num and j< size-num):
#             print("*",end="")
#         elif (i==num*2 and j>=num) or (j==num*2 and i>=num):
#             print("*", end="")
#         else:
#             print("-",end="")
#     print()

# Pattern N
# num = int(input())
# for i in range(num):
#     for j in range(num):
#         if i==j or j==0 or j==num-1:
#             print("*", end="")
#         else:
#             print("-",end="")
#     print()

#Sum to N
# num= int(input())
# total = 0
# for i in range(num+1):
#     total += i

# print(total)

#Problem 38 
# num = int(input())
# positions = list(map(int,input().split()))
# result =[]
# sorted_positions = sorted(positions)
# for i in range(len(sorted_positions)):
#     for j in range(len(positions)):
#         if sorted_positions[i]==positions[j]:
#             if str(j+1) not in result:
#                 result.append(str(j+1))
# output = " ".join(result)
# print(output)

# Problem 38 another solution with enumerate
# num = int(input())
# positions = list(map(int, input().split()))

# monsters = []

# for index, distance in enumerate(positions, 1):
#     monsters.append((distance, index))

# monsters.sort()

# result = []

# for distance, index in monsters:
#     result.append(str(index))

# print(" ".join(result))

#Problem 42 (Factor#1)
# num = int(input())
# count = 0
# for i in range(num+1):
#   if i > 0 and num%i==0:
#     count += 1
# print(count)

#Problem 43 that got partially accepted with runtime error 
# num = list(map(int, input().split()))
# num.sort()
# mid = int(len(num)//2)
# median=int(num[mid])
# result = []
# for i in range(len(num)):
#     total =0
#     for j in num:
#         total += abs(j-median)
#     if total !=0:
#         result.append(total)

# output=min(result)
# print(output)
# print("num: ", num)
# print("median:", median)
# print("result:", result)
# print("final output:", output)

#Better solution for Problem 43
# num = list(map(int, input().split()))
# num.sort()

# median = num[len(num) // 2]

# total = 0

# for j in num:
#     total += abs(j - median)

# print(total)

#Problem: Encrypt
# text = str(input()).lower()
# result = []
# for i in range(len(text)):
#     result.append(text.count(text[i]))

# for i in result:
#     if i>=2:
#         print("-",end="")
#     else:
#         print("*",end="")

#Problem 47 - CSC102 Quiz#1 2019 Weapon factory
# num = int(input())
# sw = 0
# sh = 0 
# hel = 0 
# remain = 0
# for i in range(num):
#     if num>=10:
#         num = num - 10
#         sw +=1
#     if num >= 8:
#         num = num - 8
#         sh += 1
#     if num>=3:
#         num = num -3
#         hel += 1
#     if num <3: 
#         remain = num
# print(sw, sh, hel, remain)

# A more concise way 
# num = int(input())

# sets = num // 21
# remain = num % 21

# sw = sets
# sh = sets
# hel = sets

# sw += remain // 10
# remain %= 10

# sh += remain // 8
# remain %= 8

# hel += remain // 3
# remain %= 3

# print(sw, sh, hel, remain)

#Working but my way of thinking
# states =str(input()).split()
# switches = str(input()).split()

# mur_state, dnd_state = states 
# mur_switch, dnd_switch = switches

# if mur_state=='0' and dnd_state=='0':
#     if mur_switch=='-' and dnd_switch=='-':
#         print("NEUTRAL")
#     elif mur_switch=='1' and dnd_switch=='-':
#         print("MuR")
#     elif mur_switch=='-' and dnd_switch=='1': 
#         print("DnD")
# elif mur_state=='1' and dnd_state=='0':
#     if mur_switch=='-' and dnd_switch=='-':
#         print("MuR")
#     elif mur_switch=='1' and dnd_switch=='-':
#         print("NEUTRAL")
#     elif mur_switch=='-' and dnd_switch=='1': 
#         print("DnD")
# elif mur_state=='0' and dnd_state=='1':
#     if mur_switch=='-' and dnd_switch=='-':
#         print("DnD")
#     elif mur_switch=='1' and dnd_switch=='-':
#         print("MuR")
#     elif mur_switch=='-' and dnd_switch=='1': 
#         print("NEUTRAL")

#Isogram 
# text = input()

# letters = [char.lower() for char in text if char.isalpha()]
# print(letters)
# if len(letters) == len(set(letters)):s
#     print(text, 'is an isogram')
# else:
#     print(text, 'is not an isogram')

"""
def add_setting(settings,key_value):
    key = key_value[0].lower()
    value = key_value[1].lower()
    
    if key in settings:
        return(f"Setting '{key}' already exists! Cannot add a new setting with this name.")
     
    settings[key]=value
    return(f"Setting '{key}' added with value '{value}' successfully!")

def update_setting(settings, key_value):
    key= key_value[0].lower()
    value = key_value[1].lower()
    if key in settings: 
        settings[key]=value
        return(f"Setting '{key}' updated to '{value}' successfully!")
    else: 
        return(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")

def delete_setting(settings, key):
    key = key.lower()
    if key in settings: 
        removed_key_value = settings.pop(key)
        return(f"Setting '{key}' deleted successfully!")
    else:
        return(f"Setting not found!")

def view_settings(settings):
    if not settings:
        return("No settings available.")
    else:
        result = "Current User Settings:\n"
        for key, value in settings.items():
            result += key.capitalize() + ": " + value + "\n"
        return result
        

test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}

"""


#textinsideout


