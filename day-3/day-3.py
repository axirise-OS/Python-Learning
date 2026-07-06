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