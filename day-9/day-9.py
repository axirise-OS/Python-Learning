# day - 9
# Polymorphism

# Challenge 1
# Vehicles

class Vehicle:
   def move():
      pass

class car(Vehicle):
   def move(self):
      return "Car -> Driving on the road 🚗"

class Airplane(Vehicle):
   def move(self):
      return "Airplane -> Flying in the sky ✈️"

class Boat(Vehicle):
   def move(self):
      return "Boat -> Sailing on water 🚢"

print(car.move())
print(Airplane.move())
print(Boat.move())

# Challenge 2
# Employees

class Employees():
   def __init__(self, Name, job):
      self.Name = Name
      self.job = job
   def Work():
      pass

class Programmer(Employees):
   def Work(self):
      return "Writing code..."
   
class Doctors(Employees):
   def Work(self):
      return "Treating patients..."
   
class Teacher(Employees):
   def Work(self):
      return "Teaching students..."
   
Programer1 = Programmer("Axirise" , "Programer")
Doctor1 = Doctors("Alex" , "Doctor")
Teacher1 = Teacher("Mohamed" , "Teacher")

print(f"{Programer1.Name} is a {Programer1.job} = {Programer1.Work()}")
print(f"{Doctor1.Name} is a {Doctor1.job} = {Doctor1.Work()}")
print(f"{Teacher1.Name} is a {Teacher1.job} = {Teacher1.Work()}")

# Library Management System
class Library:
   def __init__(self, is_taken, Book_health, Book_copys):
      self.is_taken = is_taken
      self.Book_health = Book_health
      self.Book_copys = Book_copys
class Books(Library):
   def __init__(self, is_taken, Book_health, Book_copys, title, author, available, Pages):
      super().__init__(is_taken, Book_health, Book_copys)
      self.title = title
      self.author = author
      self.available = available
      self.pages = Pages

Books_library = [Books(True, "good", 1, "The 1-Page Marketing Plan", "Allan Dib", False, 320),
                 Books(False, "good", 3, "Dopamine Nation", "Anna Lembke, MD", True, 304),
                 Books(False, "good", 4, "Can't Hurt Me", "David Goggins", True, 364),
                 Books(False, "good", 5, "Rich Dad Poor Dad", "Robert Kiyosaki and Sharon Lechter", True, 336)]

def Menu():
   print("----- Library -----")
   print("1- Show Books")
   print("2- Borrow Book")
   print("3- Return Book")
   print("4- Add Book")
   print("5- Exit")
   print("-------------------")

def Borrow_book(Borrow):
   for book in Books_library:
      if Borrow == book.title:
         book.Book_copys -= 1
         print("You must return the book in 24h")
         break
      else:
         X = 0
   if  X == 0:
      print("the book not found")

def Return_book(Return):
   for book in Books_library:
      if Return == book.title:
         book.Book_copys += 1
         print("Thanks for return the book")
         break
      else:
         X = 0
   if  X == 0:
      print("the book not found")

def New_book():
   is_taken = bool(input("Is it taken?: "))
   Book_health = input("Enter book health: ")
   Book_copys = int(input("How many copys?: "))
   title = input("Enter the title of the book: ")
   author = input("the author: ")
   available = bool(input("Is it available?: "))
   Pages = int(input("The numper of pages: "))
   New_book = Books(is_taken, Book_health, Book_copys, title, author, available, Pages)
   Books_library.append(New_book)

def main():
   while True:
      Menu()
      Choice = input("Enter (1 : 5): ")
      if Choice == "1":
         for book in Books_library:
            print("==================")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Available: {book.available}")
      elif Choice == "2":
         Borrow = input("Enter the name of the Book: ")
         Borrow_book(Borrow)
      elif Choice == "3":
         Return = input("Enter the name of the Book: ")
         Return_book(Return)
      elif Choice == "4":
         New_book()
      elif Choice == "5":
         break

if __name__ == "__main__":
   main()