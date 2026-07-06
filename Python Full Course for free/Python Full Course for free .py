
# Exercise 1 Rectangle Area calc
#lenght = float(input("What is the lenght?: "))
#width = float(input("What is the width?: "))
#Area = lenght * width
#print(f"The Area is: {Area}cm²")

#print("==================")

#Exercise 2 Shopping Cart program
#item = input("What is the item?: ")
#price = float(input("What is the price?: "))
#quantity = int(input("How many?: "))
##total = price * quantity
#print(f"The order is: {quantity} of {item} × ${price} ")
#print(f"total price is: ${total}")

#print("==================")

#Complet the word
#print("Complet the word")
#print("I love p.... so much")
#word = input("what is the word?: ")
#print(f"I love {word} so much")

#print("==================")

#Madlips game
#Word game where you create a story
#by filling in blanks wiht random words
#place = input("name a place: ")
#name_1 = input("name a name (friend): ")
#question = input("give a question: ")
#answer = input("answer the question: ")

#print(f"i went to {place} today")
#print(f"i saw my friend {name_1} ")
#print(f"she\he asked me: {question}")
#print(f"i sayed: {answer}")

#print("==================")

#Opetoresra
#pizza_num = 5

#pizza_num  = pizza_num + 1
#pizza_num += 1

#pizza_num  = pizza_num - 1
#pizza_num -= 1

#pizza_num  = pizza_num * 1
#pizza_num *= 1

#pizza_num  = pizza_num / 1
#pizza_num /= 1

#pizza_num  = pizza_num ** 1
#pizza_num **= 1

#pizza_num  = pizza_num % 1

#X = 5
#Y = -7
#Z = 6.2

#Result = round(Z)----->turn 6.2 to 6 
#Result = abs(Y)--------> turn - to +
#Result = pow(4 , 3)---> 4 * 4 * 4
#Result = max(4 , 3)---> give the max 6.2
#Result = min(4 , 3)---> give the min -7

#==================

#Maht
#import math
#F = 5
#print(math.pi)
#print(math.e)
#print(math.sqrt(F))
#print(math.ceil(4.1))----> 5
#print(math.floor(4.9))----> 4

#Exercis C=2pi*r
#import math
#r = float(input("What is the redius of the circle?: "))
#pi = math.pi
#C = 2 * pi * r 
#C = 2 * math.pi * r ------> another way to write it
#print(f"The c is : {C}")

#=====================

#Exercise A = pi*r²
#import math
#r = float(input("What is the redius of the circle ?: "))
#A = math.pi * r**2
#A = math.pi * pow(r , 2)------->another way to write it
#print(f"The A is: {A}")

#=====================

#Exercise C = جزر a² + b²
#import math
#A = float(input("What is the tall of A?: "))
#B = float(input("What is the tall of B?: "))
#plus = pow(A , 2) + pow(B , 2)
#C = math.sqrt(plus)
#C = math.sqrt(pow(A ,2) + pow(B , 2))------> another way to write it
#print(C)

#=====================

# IF condition 
#score = int(input("What is your score?: "))
#if score >= 50 :
   #print("You are winer")
#elif score < 0 :
    #print("How?????")
#else :
   # print("You are loser")

#=====================

# python calculator
#import math
#Num_circle = input("What u wanna calculat (1.Nums & 2.circle) ?: ")
#if Num_circle == "1" :

 #   type_cal = input("What is the type of calculator(- + * /)?: ")
   
#elif Num_circle == "2" :

 #   type_cal = input("What is the type of calculator(1.Area & 2.circum)?: ")

#else:
# print("write the right numper pls!")
#exit()


#cal = type_cal

#if cal == "-":
 #   num_1 = float(input("What is the first num?: "))
  #  num_2 = float(input("What is the scound num?: "))
   # result = num_1 - num_2
    #print(round(result, 3))

#elif cal == "+":
 #   num_1 = float(input("What is the first num?: "))
  #  num_2 = float(input("What is the scound num?: "))
   # result = num_1 + num_2
   #print(round(result, 3))

#elif cal == "*":
 #   num_1 = float(input("What is the first num?: "))
  #  num_2 = float(input("What is the scound num?: "))
   # result = num_1 * num_2
    #print(round(result, 3))

#elif cal == "/":
 #   num_1 = float(input("What is the first num?: "))
  #  num_2 = float(input("What is the scound num (!= 0)?: "))
   # result = num_1 / num_2
    #print(round(result, 3))

#elif cal == "1":
 #   reduis = float(input("What is the reduis?: "))
  #  C = math.pi * 2 * reduis
  # print(round(C,3))

#elif cal == "2":
 #   reduis = float(input("What is the reduis?: "))
  #  A = math.pi * pow(reduis , 2)
   # print(round(A,3))

#else:
 #   print("write the right choies pls")
  #  exit()

#python weight converter
#weight = float(input("What is ur weight?: "))
#unit = input("kilograms or Pounds (K & P)?: ")
#if unit.lower() == "k" :
    #print(f"Your weight in pounds: {round(weight * 2.205 , 3)}")
#elif unit.lower() == "p":
    # print(f"Your weight in Kilograms: {round(weight / 2.205 , 3)}")
#else:
   #  print("wirte K or P pls")

#Universal Converter
#print("=== Universal Converter ===")
#print("1 - Weight")
#print("2 - Temperature")
#print("3 - Length")
#choice = input("Choose(1 - 2 - 3): ")
#if choice == "1":
 ##   print("=== Weight ===")
 #   POUNDS_PER_KG = 2.205
 #   weight = float(input("Enter your weight: "))
 #   print("Choose the unit:")
 ##   print("1 - kilograms ")
 #   print("2 - Pounds")
 #   unit = input("Choose(1 - 2): ")
   # if unit == "1":
     #   print(f"Your weight is: {round(weight*POUNDS_PER_KG, 3)} Pound")
    #elif unit == "2":
     #   print(f"Your weight is: {round(weight/POUNDS_PER_KG, 3)} Kg")
   # else:
      #  print("you have to writh just '1' or '2'")
      #  exit()
#elif choice == "2":
  # print("=== Temperature ===")
 #  temperature = float(input("Enter the Temperature:"))
  # print("Choose the unit:")
#   print("1 - Celsius")
 #  print("2 - Fahrenheit")
 #  unit = input("Choose(1 - 2): ")
 #  if unit == "1":
 #      print(f"your Temperature is: {round((temperature * 9 / 5 ) + 32, 3 )} Fahrenheit" )
 #  elif unit == "2":
 #      print(f"your Temperature is: {round((temperature - 32) * 5 / 9 , 3 )} Celsius" )
 #  else:
  #     print("you have to writh just '1' or '2'")
  #     exit()
#elif choice == "3":
  #  print("=== Length ===")
  #  m_per_cm = pow(10, 2)
  #  cm_per_m = pow(10, -2)
  #  length = float(input("Enter your Length: "))
  #  print("Choose the unit:")
  #  print("1 - M")
  # print("2 - Cm")
   # unit = input("Choose(1 - 2): ")
   # if unit == "1":
       # print(f"your Length is: {round(length*cm_per_m, 3)} Cm ")
    #elif unit == "2":
        #print(f"your Length is: {round(length*m_per_cm, 3)} M ")
    #else:
       # print("you have to writh just '1' or '2'")
        #exit()
#else:
   # print("you have to writh just '1' or '2' or '3'")
   # exit()

#================
#day - 3
#logical operators (or , and , not)

# or = at least one condition is true
# and = both condition must be true
# not = inverts the condition ( not true , not false)

temp = 5
is_sunny = False
is_raning = False

if (temp <= 40 and temp >= 25) and is_sunny :
    print("you can go to swim 🏊")

elif (temp <= 25 and temp >= 15 ) and not is_raning:
    print("you can go to walk 🚶")

elif (temp <= 14 and temp >= 1) and is_raning == False :
    print("ware winter clothes🥼")

elif temp <= 0 or is_raning == True:
    print("stay at home 🏡")
else:
    exit()

# Short if 
#X if condition else Y

num1 = -1
print("positive" if num1 >= 0 else "negative" )

#===========
#String method

#_name_ = input("Enter your name?: ")
#phone_numper= input("Enter your phone_numper?: ")

#result = len(_name_)
#result = _name_.find("A")-----------> find first index "A"
#result = _name_.rfind("A")--------> find last index of "A"
#result = _name_.capitalize()----> make first cracter Capital
#result = _name_.upper()--------> make all cracters upper case
#result = _name_.lower()----------> make all cracters lower case
#result = _name_.isdigit()--------> print("true" if _name_ == nums else "false")
#result = _name_.isalpha()--------> print("true" if _name_ == alpha else "false")

#result = phone_numper.count("-")-------> count how many "-" in the input
#result = phone_numper.replace("-" , " ")-------> replace "-" with " "

#print(result)

#============

# validte user input exercise
name = input("Enter your name(12/12 long | no spaces | no numpers)?: ")
name_long = len(name)
name_space = name.count(" ")
name_digit = name.isalpha()

if name_long <= 12 and name_space == 0 and name_digit == True:
    print(" Your name accepted!")

elif name_long >= 12  and name_space == 0 and name_digit == True:
    print("You must writ a name have 12 cracter maximum")
    print(f"You have entered {name_long} cracter")

elif name_long <= 12 and name_space > 0 and name_digit == True:
    print(f"Your name have {name_space} space")

elif name_long <= 12 and name_space == 0 and name_digit == False:
    print(f"Your name have anoter cracter with alphas")

else:
    print("your name have many mistakes")
    print("pls read the rools and try again !")

#============

#indaxing
#find middel game
import math
mid_game = input("Enter anything to find the middel carcter: ")
index = int(len(mid_game))
remainder = index % 2
Even_1 = int((index / 2) + 1)
Even_2 = int((index / 2) - 1)
Odd = math.floor(index / 2)
if remainder == 0:
    
   print(f"the mid cracter is: {mid_game[Even_2 : Even_1]}")

else:
    print(f"the mid cracter is: {mid_game[Odd]} ")


#===============

#Text Analyzer
import math
Text_Analyzer = input("Enter Your text: ")
index = len(Text_Analyzer)
remainder = index % 2

print(f"numper of cracters: {index}")
print(f"first cracter: {Text_Analyzer[0]}")
print(f"last cracter: {Text_Analyzer[-1]}")
print(f"first 3 cracters: {Text_Analyzer[0 : 3]}")
print(f"last 3 cracters: {Text_Analyzer[-3 :]}")

left_mid = math.floor(index / 2) - 1
right_mid = math.floor(index / 2) + 1
mid = math.floor(index / 2)

if remainder == 0:
    print(f"Your mid cracter is: {Text_Analyzer[left_mid : right_mid]}")

else:
    print(f"Your mid cracter is: {Text_Analyzer[mid]}")

#===============


#while loop
age = int(input("Enter your age?: "))
while age < 0 :
    print("age can`t be negative!")
    age = int(input("Enter your age?: "))
print(f"your age is: {age}")

#================

#python compound interest calculator
continue_= "y"
while not continue_ == "n" :
 p = float(input("How money do u have?: "))
 while not p > 0:
    print("you must enter numper biger then '0' ")
    p = float(input("How money do u have?: "))

 r = float(input("How much Interest Rate u will get?: "))
 while not r > 0:
    print("you must enter numper biger then '0%' ")
    r = float(input("How much Interest Rate u will get?: "))

 Rate = (r /100)

 n = int(input("how many tiems u will get Interest?: "))
 while not n > 0 :
    print("you must enter numper biger then '0' ")
    n = int(input("how many tiems u will get Interest?: "))

 t = int(input("how many years?: "))
 while not t > 0:
    print("you must enter numper biger then '0' ")
    t = int(input("how many years?: "))

 A = p * pow((1 + Rate / n ), t)

 print("========== RESULT ==========")
 print("")
 print(f"Principal : ${p}")
 print("")
 print(f"Rate      : {r}%")
 print("")
 print(f"Years     : {t}")
 print("")
 print(f"Final     : ${round(A, 2)}")
 print("")
 print("============================")
 continue_ = input("do u wanna try again (Y \ N)?: ")
 continue_ = continue_.lower()
 while not continue_ == "n" and not continue_ == "y":
     continue_ = input("do u wanna try again (Y \ N)?: ")
print("bye bye")

#===========

# day - 4
#for loop
for i in range(1, 11):
    print(i)

# Multiplication table - level 3
Multiplication_table = int(input("Enter any numper from (0 to 12): "))
while Multiplication_table < 0 or Multiplication_table >= 13 :
    Multiplication_table = int(input("Enter any numper from (0 to 12): "))

for i in range(1, 13):
     print(f"the Multiplication table of {Multiplication_table} is: {i} * {Multiplication_table} = {i * Multiplication_table} ")

#Collection Program level - 4
Collection_Program = int(input("Enter any numper biger the 0 : "))
while Collection_Program < 0:
    Collection_Program = int(input("Enter any numper biger the 0 : "))
Collection = 0
for i in range(1, (Collection_Program + 1)):
    Collection = Collection + i 
print(f"The Collection is {Collection}")

#level - 5
stars = int(input("Enter any numper biger then '0': "))
while stars <= 0:
    stars = int(input("Enter any numper biger then '0': "))
Y = "*"
for i in range(1 , (stars + 1)):
    print(f"{i} : ", end="")
    for X in range(1 , stars + 1):
        print(f"{Y}", end="" )
        if  X == i:
            break
        
    print("")

#level - 6
stars = int(input("Enter any numper biger then '0': "))
while stars <= 0:
    stars = int(input("Enter any numper biger then '0': "))

Y= "*"
for i in reversed(range(1 , (stars + 1))):
    print(f"{i} : ", end="")
    for X in range(1 , stars + 1):
         print(f"{Y}", end="" )
         if  X == i:
          break
       
    print("")

#count downe time programe
import time
T = "y"
while T == "y":
 time_count = int(input("Enter your time(by minutes): "))
 for i in range((time_count * 60) , 0 , -1):
    seconds = i % 60
    minutes =int( i / 60 ) % 60
    hours = int(i / 3600) % 60
    print(f"Time count downe: {hours:02} : {minutes:02} : {seconds:02}")
    time.sleep(1)
 print("Finished")
 T = input("(Y : N)?: ")
 T.lower()
 while not T == "y" and not T == "n" :
  T = input("(Y : N)?: ")
  T.lower()

#collection
#list-----> [] ordered and changeable , duplicates
# X = [1 , 2 , 3 , 4]
# print(dir(X))
# print(help(X))
# print(len(X))
# print(1 in X)
# print(sort(X))
# print(append(X))
# print(remove(X))
# print(update(X))
# print(X[0])
# print(X[0] = 5)
# print(x.insert(2, 9))
# print(x.reverse())
# print(x.clear())
# print(x.index("1"))
# print(x.count("1"))

#set -----> {} unorfered and immutable, but add\remove ok , no duplicates
# X = {1 , 2 , 3 , 4}
# print(dir(X))
# print(help(X))
# print(len(X))
# print(1 in X)
# print(X.add(12))
# print(X.remove(1))
# print(X.pop())--------> remover whatever is the first in the set
# print(X.clear)

#Tuple = () ordered and unchangeable , duplicates ok , faster
# X = (1 , 2 , 3 , 4)
# print(dir(X))
# print(help(X))
# print(len(X))
# print(1 in X)
# print(X.index(0))
# print(X.count(2))

#=============

#shopping cart program
foods = []
price = ( 1 , 2 , 3 , 4 , 5)
total = 0
while True:
    food = input("Eentr your food(Q to quit): ")
    if food.lower() == "q":
     break
    else:
     foods.append(food)
     print(food)

index = len(foods)
for i in range(0 , (index - 1)):
 total = total + price[index % len(price)]
print(total)

# 2D list 
# list = [list1 , list2 , list3]
list1 = [1 , 2 , 3]
list2 = [4 , 5 , 6]
list3 = [7 , 8 , 9]
list_2D = [list1 , list2 , list3]
print(list_2D[0][0])

# 2D tuple example 
# list = [list1 , list2 , list3]
tuple1 = (1 , 2 , 3)
tuple2 = (4 , 5 , 6)
tuple3 = (7 , 8 , 9)
tuple4 = ("*" , 8 , "#")
tuple_2D = (tuple1 , 
            tuple2 , 
            tuple3 , 
            tuple4)
for row in tuple_2D:
 for num in row :
   print(num, end=" ") 
 print() 

# Python quiz game

questions =("How many elements are in the peridic table?: " ,
            "Which animal lays the largest eggs?: " ,
            "What is the most abundant gas un Earth`s atmosphere?: " ,
            "How many bones are in the human body?: " ,
            "Which planet in the solar system is the hottest?: ")

options =(("A. 116", "B. 117", "C. 118", "D. 119"),
          ("A. Whale", "B. Crocodile", "C. Elphant", "D. Ostrich"),
          ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
          ("A. 206", "B. 207", "C. 208", "D. 209"),
          ("A. Marcuy", "B. venus", "C. Earth", "D. Mars"))

answers =("C", "D", "A", "A", "B")
gusses =[]
score = 0
question_num = 0

for question in questions:
  print("------------------------")
  print(question)
  for option in options[question_num]:
    print(option)

  guess = input("Enter (A , B , C , D): ").upper()
  gusses.append(guess)
  if gusses[question_num] == answers[question_num]:
     print("Corect !!")
     score += 1
  else:
     print("Wrong !!")
  question_num += 1

score = (score / len(questions)) * 100
print(f"Your score is: {score}%")
