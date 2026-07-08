# day-5
#dictionary = collection of (key : value) ordered and changeable and no duplicat 

price = {"pizza": 10.99 , "Rice" : 2.99 , "banana" : 5.99}
print(dir(price))
print(help(price))
price.pop("banana")#------- remove the first item
price.popitem()#------- remove the latest item
price.clear()
print(price.update({"Rice" : 2.22}))
print(price.get("pizza"))
print(price.keys(price))
print(price.values(price))
print(price.items())

# Concession stand programe

concessions = {"pupcorn": "1.00" ,
               "hot dog": "2.00" ,
               "giant pretzel": "3.00" ,
               "asst candy": "4.00" ,
               "soda": "5.00" ,
               "bottled water": "6.00" ,}
price = 0
while True:
 person_want = input("Enter (Menu , Food)(Q to quit)?: ").lower()
 if person_want == "menu":
    for key , value in concessions.items():
     print(f"the Menu is: {key} : ${value}")

 elif person_want == "food":
   food = input("search about: ")
   if concessions.get(food):
     print(f"the price is: {concessions.get(food)}")
   else:
     print("the food dosn`t exiect")
            
 elif person_want == "q":
   break
   
# Concession stand programe v.22

menu = {"pupcorn": 1.00 ,
        "hot dog": 2.00 ,
        "giant pretzel": 3.00 ,
        "asst candy": 4.00 ,
        "soda": 5.00 ,
        "bottled water": 6.00 ,}
card =[]
total = 0
print("----------the menu----------")
for keys , values in menu.items():
   print(f"{keys:15} : ${values:.2f}")
print("----------------------------")
while True:
   food = input("What food You like to buy?(Q to Quit and B to Buy): ").lower()
   if menu.get(food):
    card.append(food)
    total = total + menu.get(food)
   else:
    if food == "b":
     print(f"you have buy: {card}")
     print(f"The total price is: {total:.2f}")
    elif food == "q":
      break
    else:
      print("this food dosen`t found !!")

# import random
import random
low = 0 
high = 100
card = ["1","2","3","4","5","6","7","8"]
num_int = random.randint(low,high)
num_float0_1 = random.random()
option = random.choice(card)
numper = random.shuffle(card)

print(num_int)
print(num_float0_1)
print(option)
print(card)

#numper gussing game
import random

low = int(input("Enter the low num: "))
high = int(input("Enter the high num: "))
running = True
numper = random.randint(low, high)
while running:
 guess = int(input(f"Enter numper bettwen {low} : {high} (q to quit): "))
 if guess == numper:
    print("the guess is right!!")
    running = False
 elif guess > numper:
   print(f"The numper is less then {guess}")
 elif guess < numper:
   print(f"The numper is more then {guess}")

# function
def hello_world():
   print("hello world")
hello_world()