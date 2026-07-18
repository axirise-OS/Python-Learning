# day - 10 

# instance methods
class instance:
   def __init__(self, Name, ID):
      self.Name = Name
      self.ID = ID
   
   def get_info(self):
      return f"The Name is: {self.Name} and the ID is: {self.ID}"
# @Static methods
   @staticmethod
   def Static_methods(Name, ID):
      Name_x = ["Assem", "Radjaa"]
      ID_x = ["3300", "3301"]
      return Name in Name_x and ID in ID_x
   
User_1 = instance("Radjaa", "3301")
print(User_1.get_info())
print(instance.Static_methods("Assem", "3300"))

# @class methods
class Student:
   Count = 0
   toral_GPA = 0
   def __init__(self, Name, ID, GPA):
      self.Name= Name
      self.ID= ID
      self.GPA= GPA
      Student.Count += 1
      Student.toral_GPA += GPA
   def get_info(self):
      return f"{self.Name} : {self.ID} / {self.GPA}"
   @classmethod
   def get_count(cls):
      return f"total student is: {Student.Count}"
   @classmethod
   def get_avrage_GPA(cls):
      if Student.Count == 0:
         return 0
      elif Student.Count > 0:
         return f"Average GPA is: {Student.toral_GPA / Student.Count :.2f}"
      
Student1 = Student("Assem", "3300", 4.0)
Student2 = Student("Radjaa", "3301", 4.0)
Student3 = Student("Wasyla", "3302", 4.0)
print(Student1.get_info())
print(Student2.get_info())
print(Student3.get_info())
print(Student.get_count())
print(Student.get_avrage_GPA())

# Magic methods
class Books:
   def __init__(self, Title, Author, Pages):
      self.Title = Title
      self.Author = Author
      self.pages= Pages
   def __str__(self):
      return f"Title: {self.Title} Author: {self.Author}"
   def __eq__(self, other):
      return self.Title == other.Title and self.Author == other.Author
   def __lt__(self, other):
      return self.pages < other.pages
   def __gt__(self, other):
      return self.pages > other.pages
   def __add__(self, other):
      return self.pages + other.pages
   def __contains__(self, Keyword):
      if Keyword in self.Title:
       return self.Title
      elif Keyword in self.Author:
         return self.Author
   def __getitem__(self, key):
      if key == "Title":
         return self.Title
      elif key == "Author":
         return self.Author
      elif key == "pages":
         return self.pages
      else:
         return f"The {key} is not found!"
   def __len__(self):
      return self.pages
Book1 = Books("Dopamine Nation", "Anna Lembke, MD", 304 )
Book2 = Books("Clear Thinking", "Shane Parrish", 288 )

print(Book1)
print(Book2)
print(Book1 + Book2)
print(Book1 > Book2)
print(Book1 < Book2)
print("Dopamine" in Book1)
print("Parrish" in Book2)
print(Book1["Title"])
print(Book2["pages"])
print(len(Book1))
print(len(Book2))

# @property
# Getter & Setter & Deleter
class Rectangle:
   def __init__(self, width, hight):
      self._width = width
      self._hight = hight
   
   @property
   def width(self):
      return f"{self._width} cm²"
   @property
   def hight(self):
      return f"{self._hight} cm²"
   @width.setter
   def width(self, New_width):
      if New_width > 0:
         self._width = New_width
      else:
         raise ValueError("The width must be grater then '0'")
   @hight.setter
   def hight(self, New_hight):
      if New_hight > 0:
         self._hight = New_hight
      else:
         raise ValueError("The hight must be grater then '0'")
   @width.deleter
   def width(self):
      del self._width
      print("width have been deletd")
   @hight.deleter
   def hight(self):
      del self._hight
      print("hight have been deletd")
Rectangle1 = Rectangle(6,7)
Rectangle1.width = 1
print(Rectangle1.width)
print(Rectangle1.hight)
del Rectangle1.width
del Rectangle1.hight

# Docorator
def add_thing(func):
   def wrapper(thing):
      print("you add thing!!")
      func(thing)
   return wrapper

@add_thing
def something(thing):
   print(f"Here is your {thing}")

something("anything")

# Exceptions
try:
   num = int(input("Enter a numper: "))
   print( 1 / num)
except ZeroDivisionError:
   print("You cant divide by zero")
except ValueError:
   print("Enter only numpers")
except Exception:
   print("Someting went worng!!")
finally:
   print("Done!!")

# Python file detection
import os
file_path = "C:\\Users\\Axiri\\Developer\\Python-Learning\\hello.py"
if os.path.exists(file_path):
   print("File found!!")
   if os.path.isfile(file_path):
    print("its a file!!")
   elif os.path.isdir(file_path):
      print("its a directory!!")
else:
   print("File not found!!")

# python writing files (.txt , .json , .csv)
# tomorrow