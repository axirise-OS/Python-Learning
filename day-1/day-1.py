# Exercise 1 Rectangle Area calc
lenght = float(input("What is the lenght?: "))
width = float(input("What is the width?: "))
Area = lenght * width
print(f"The Area is: {Area}cm²")

#print("==================")

#Exercise 2 Shopping Cart program
item = input("What is the item?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many?: "))
total = price * quantity
print(f"The order is: {quantity} of {item} × ${price} ")
print(f"total price is: ${total}")

#print("==================")

#Complet the word
print("Complet the word")
print("I love p.... so much")
word = input("what is the word?: ")
print(f"I love {word} so much")

#print("==================")

#Madlips game
#Word game where you create a story
#by filling in blanks wiht random words
place = input("name a place: ")
name_1 = input("name a name (friend): ")
question = input("give a question: ")
answer = input("answer the question: ")

print(f"i went to {place} today")
print(f"i saw my friend {name_1} ")
print(f"she\he asked me: {question}")
print(f"i sayed: {answer}")

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
import math
F = 5
print(math.pi)
print(math.e)
print(math.sqrt(F))
#print(math.ceil(4.1))----> 5
#print(math.floor(4.9))----> 4

#Exercis C=2pi*r
import math
r = float(input("What is the redius of the circle?: "))
pi = math.pi
C = 2 * pi * r 
#C = 2 * math.pi * r ------> another way to write it
print(f"The c is : {C}")

#=====================

#Exercise A = pi*r²
import math
r = float(input("What is the redius of the circle ?: "))
A = math.pi * r**2
#A = math.pi * pow(r , 2)------->another way to write it
print(f"The A is: {A}")

#=====================

#Exercise C = جزر a² + b²
import math
A = float(input("What is the tall of A?: "))
B = float(input("What is the tall of B?: "))
plus = pow(A , 2) + pow(B , 2)
C = math.sqrt(plus)
#C = math.sqrt(pow(A ,2) + pow(B , 2))------> another way to write it
print(C)
