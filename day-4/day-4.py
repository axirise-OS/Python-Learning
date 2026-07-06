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
