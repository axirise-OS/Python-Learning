#day - 12
# multithreading
import threading
import time

def Go_sleep(Name, age):
   time.sleep(3)
   print(f"You have went to sleep {Name} and your age is {age}")
def Go_shoping(item):
   time.sleep(3)
   print(f"You have went to shoping {item}")
def Go_GYM():
   time.sleep(3)
   print("You have went to GYM")

chore1 = threading.Thread(target= Go_sleep, args=("Axirise", "XX"))
chore1.start()
chore2 = threading.Thread(target= Go_shoping, args=("meat",))
chore2.start()
chore3 = threading.Thread(target= Go_GYM,)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("all chores are completed")

# request API data
import requests
pokeAPI = "https://pokeapi.co/api/v2/"
def Get_poke_info(poke_name):
   url = f"{pokeAPI}/pokemon/{poke_name}"
   response = requests.get(url)
   if response.status_code == 200:
      print("We get respone 👽")
      data_poke = response.json()
      return data_poke
   elif response.status_code == 404:
      print(f"Pokemon {poke_name} was not found.")
   else: 
      print(f"faild: {response.status_code}")

def main():
 poke_name = input("Enter the name of pokemon: ").lower()
 pokemon_info = Get_poke_info(poke_name)
 if pokemon_info:
   print(f"Name :{pokemon_info["name"]}")
   print(f"ID : {pokemon_info["id"]}")
   print(f"Height : {pokemon_info["height"]}")
   print(f"Weight : {pokemon_info["Weight"]}")
   print(f"Base Experience : {pokemon_info["Base_Experience"]}")
 else:
      print("data not found")
main()