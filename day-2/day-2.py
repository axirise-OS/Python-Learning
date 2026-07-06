# IF condition 
score = int(input("What is your score?: "))
if score >= 50 :
   print("You are winer")
elif score < 0 :
    print("How?????")
else :
    print("You are loser")

#=====================

# python calculator
import math
Num_circle = input("What u wanna calculat (1.Nums & 2.circle) ?: ")
if Num_circle == "1" :

    type_cal = input("What is the type of calculator(- + * /)?: ")
   
elif Num_circle == "2" :

    type_cal = input("What is the type of calculator(1.Area & 2.circum)?: ")

else:
    print("write the right numper pls!")
    exit()


cal = type_cal

if cal == "-":
    num_1 = float(input("What is the first num?: "))
    num_2 = float(input("What is the scound num?: "))
    result = num_1 - num_2
    print(round(result, 3))

elif cal == "+":
    num_1 = float(input("What is the first num?: "))
    num_2 = float(input("What is the scound num?: "))
    result = num_1 + num_2
    print(round(result, 3))

elif cal == "*":
    num_1 = float(input("What is the first num?: "))
    num_2 = float(input("What is the scound num?: "))
    result = num_1 * num_2
    print(round(result, 3))

elif cal == "/":
    num_1 = float(input("What is the first num?: "))
    num_2 = float(input("What is the scound num (!= 0)?: "))
    result = num_1 / num_2
    print(round(result, 3))

elif cal == "1":
    reduis = float(input("What is the reduis?: "))
    C = math.pi * 2 * reduis
    print(round(C,3))

elif cal == "2":
    reduis = float(input("What is the reduis?: "))
    A = math.pi * pow(reduis , 2)
    print(round(A,3))

else:
    print("write the right choies pls")
    exit()

#python weight converter
weight = float(input("What is ur weight?: "))
unit = input("kilograms or Pounds (K & P)?: ")
if unit.lower() == "k" :
    print(f"Your weight in pounds: {round(weight * 2.205 , 3)}")
elif unit.lower() == "p":
    print(f"Your weight in Kilograms: {round(weight / 2.205 , 3)}")
else:
    print("wirte K or P pls")

#==================

#Universal Converter
print("=== Universal Converter ===")
print("1 - Weight")
print("2 - Temperature")
print("3 - Length")
choice = input("Choose(1 - 2 - 3): ")
if choice == "1":
    print("=== Weight ===")
    POUNDS_PER_KG = 2.205
    weight = float(input("Enter your weight: "))
    print("Choose the unit:")
    print("1 - kilograms ")
    print("2 - Pounds")
    unit = input("Choose(1 - 2): ")
    if unit == "1":
        print(f"Your weight is: {round(weight*POUNDS_PER_KG, 3)} Pound")
    elif unit == "2":
        print(f"Your weight is: {round(weight/POUNDS_PER_KG, 3)} Kg")
    else:
        print("you have to writh just '1' or '2'")
        exit()
elif choice == "2":
   print("=== Temperature ===")
   temperature = float(input("Enter the Temperature:"))
   print("Choose the unit:")
   print("1 - Celsius")
   print("2 - Fahrenheit")
   unit = input("Choose(1 - 2): ")
   if unit == "1":
       print(f"your Temperature is: {round((temperature * 9 / 5 ) + 32, 3 )} Fahrenheit" )
   elif unit == "2":
       print(f"your Temperature is: {round((temperature - 32) * 5 / 9 , 3 )} Celsius" )
   else:
       print("you have to writh just '1' or '2'")
       exit()
elif choice == "3":
    print("=== Length ===")
    m_per_cm = pow(10, 2)
    cm_per_m = pow(10, -2)
    length = float(input("Enter your Length: "))
    print("Choose the unit:")
    print("1 - M")
    print("2 - Cm")
    unit = input("Choose(1 - 2): ")
    if unit == "1":
        print(f"your Length is: {round(length*cm_per_m, 3)} Cm ")
    elif unit == "2":
        print(f"your Length is: {round(length*m_per_cm, 3)} M ")
    else:
        print("you have to writh just '1' or '2'")
        exit()
else:
    print("you have to writh just '1' or '2' or '3'")
    exit()