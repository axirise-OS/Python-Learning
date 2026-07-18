# day-7
#Encrypted program

import random
import string

chars = "" + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

input_user = input("Enter any massage: ")

Encrypteed =""
for letter in input_user:
  index = chars.index(letter)
  Encrypteed += key[index]

print(Encrypteed)

input_user_X = input("Enter any massage to encrypted: ")

Encrypteed_x =""
for letter in input_user_X:
  index = key.index(letter)
  Encrypteed_x+= chars[index]

print(Encrypteed_x)



#=========================================================

# 5 Challenges 

#Challenge 1
# Student Grade Manager
while True:
  degree = input("Enter your degree: ")
  if degree.isdigit():
    degree = int(degree)
    if degree > 100:
     print("You show enter a numper ( 100 : 0)")
    else:
     break
  else:
    print("You show enter a numper ( 100 : 0)")
if degree >= 90:
  print("Highest")
elif degree < 90 and degree >= 75 :
  print("Average")
elif degree < 75 and degree >= 65 :
  print("Lowest")
elif degree < 65 and degree >= 50 :
  print("Passed")
elif degree < 50 and degree >= 0 :
  print("Failed")


# Challenge 2
# Password Strength Checker
score = 0
while True:
  password = input("Enter a password: ")
  if len(password) >= 4 and len(password) <= 16:
     break
  else:
     print("your password must be (4 : 16) long")

chars= ("-", "_", ".")

if len(password) > 4 and len(password) <= 7:
   score += 1
elif len(password) > 7 and len(password) <= 12:
   score += 2
else:
   score += 3


if password.find("-") or password.find("_") or password.find("."):
  score += 1
else:
   score -= 1

if not password.isalpha() and not password.isdigit():
   score += 1
else:
   score -= 1

if score >= 4:
   print("password is Strong")

elif score >= 2:
   print("password is Medium")

elif score < 2 :
   print("password is weak")


#Challenge 3
#Mini ATM

def menu():
   print("----- Mini ATM -----")
   print("1. Show balance")
   print("2. Deposit")
   print("3. Withdraw")
   print("4. History")
   print("5. Exit")
   print("--------------------")


Deposit_history = []
Withdraw_history = []
def Deposit():
   money_Deposit = int(input("How mush money you wanna Deposit?: "))
   Deposit_history.append(money_Deposit)
   return money_Deposit
def Withdraw():
   money_Withdraw = int(input("How mush money you wanna Withdraw?: "))
   Withdraw_history.append(money_Withdraw)
   return money_Withdraw
def History():
   Deposit_Times = len(Deposit_history)
   Withdraw_Times = len(Withdraw_history)
   print(f"you have Deposit {Deposit_Times} times")
   print(f"you have Withdraw {Withdraw_Times} times")
   print("choose '1' to show Deposit history ")
   print("choose '2' to show Withdraw history ")
   while True:
     History_choice = input("Enter your choice?: ")
     if History_choice == "1" :
       print(Deposit_history)
       break
     elif History_choice == "2" :
       print(Withdraw_history)
       break
def main():
   Balance = 0.0
   while True:
    menu()
    Choice = input("Enter your choice: ")
    if Choice == "1":
      print(f"You have ${Balance} in your Balance")
    elif Choice == "2":
      Balance += Deposit()
    elif Choice == "3":
      Balance -= Withdraw()
    elif Choice == "4":
      History()
    elif Choice == "5":
      break

main()
# i have problem with what if users enter anything they shoud not
#  i also have problem with local and glopal valiables



#Challenge 4
#Text Statistics

User_input = input("Enter any text: ")
print(User_input)
list(User_input)
for letter in User_input:
    print(letter , end=" ")
print()

for digit in User_input:
   if digit.isdigit():
      print(digit, end=" ")
print()

for Space in User_input:
   if Space == " ":
      print("there is a Space")
print()

for Uppercase in User_input:
   if Uppercase.upper():
      print(Uppercase, end=" ")
print()

for Lower in User_input:
   if Lower.lower():
      print(Lower, end=" ")
print()
# i have problem with upper and lower cas and Most repeated character

# Challenge 5
#Secret Diary
# i didnt study it yet

# day - 8 
# object & class