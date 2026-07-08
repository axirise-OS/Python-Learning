# day-6
#mathc case (switch)
def days_week(day):
 match day:
    case 1:
       return "saterday"
    case 2:
       return "sunday"
    case 3:
       return "monday"
    case 4:
       return "Tuesday"
    case 5:
       return "Wednesday"
    case 6:
       return "Thursday"
    case 7:
       return "Firday"  
    case _:
       return "It`s not a day"
days_week(1)
days_week(2)
days_week(3)
days_week(4)
days_week(5)
days_week(6)
days_week(7)

# import module ---------- a file containing code u want to use 
# it can be build-in or your own
# print(help(module)) 

#variable scope
#scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in


#if _name_ == "_main_"

#python Banking program
Balance = 0
amount = 0.0
is_runing = True
def Banking_program():
   print("-------Banking program---------")
   print("1. Show Balance")
   print("2. Enter money")
   print("3. Exit")
   print("-------------------------------")

def User_input():
   while True:
    User_input = int(input("Enter your choice: "))
    if User_input == 1 or User_input == 2 or User_input == 3 :
       User_input_x = User_input
       break
   return User_input_x

def Case_X(User_input_x): 
   match User_input_x:
     case 1:
       global Balance
       print(f"You have ${Balance} in your Balance: ")
     case 2:
      while True:
       money_x = float(input("Enter the money u like to add to your Balance: "))
       if money_x:
        Balance += money_x
        break    
     case 3:
       global is_runing  
       is_raning = False

while is_runing:
  Banking_program()
  CHOICE = User_input()
  Case_X(CHOICE)
      
# python Slot machine
#  ☠️👻👽☀️🏡❄️
import random

def try_again():
  is_runing = True
  while is_runing:
   try_again = input("Do u wanna spin again (Y & N)?: ").upper()
   if try_again == "Y":
     is_runing = False
     return try_again
   elif try_again == "N":
     is_runing = False
     return try_again

def slot_machine(spin):
 slots = ("☠️", "👻", "👽", "☀️", "🏡", "❄️")
 for i in range(0, spin):
   index = random.randint(0 , 6)
   return slots[index]

def Balance():
   money = 100
   is_running = True
   time_spining = 0
   while is_running:
    
    spining = int(input("how many spining you like to spin?: "))
    if spining > 0 and spining <= money:
      money -= spining
      time_spining = spining
      is_running = False
      return time_spining
    else:
      print(f"Enter nume betwen (1 : {money})")

def main():
 is_running = True
 while is_running:
   spin = Balance()
   slot1 = slot_machine(spin)
   slot2 = slot_machine(spin)
   slot3 = slot_machine(spin)
   print("----Slot machine-----")
   print(f" {slot1} | {slot2} | {slot3} ")
   print("---------------------")

   if slot1 == slot2 == slot3:
     print("You have won!!")
     if try_again() == "N":
       is_running = False
   else:
     print("you lost this round")
     if try_again() == "N":
       is_running = False

main()
