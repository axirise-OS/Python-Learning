# day - 8 
# object & class

# Mobile Phone
class Phone :
   def __init__(self, Brand, Model, Price):
      self.Brand = Brand
      self.Model = Model
      self.Price = Price

Samsung_S25 = Phone("Samsung" , "Galaxy S25 ", 48,400.00 )
iPhone_17 = Phone("Appel" , "iPhone 17 ", 69,900.00 )
      
print(Samsung_S25.Brand)
print(Samsung_S25.Model)
print(Samsung_S25.Price)

print(iPhone_17.Brand)
print(iPhone_17.Model)
print(iPhone_17.Price)


# Challenge 2
# Pet

class Pet:
   age = 2

   def __init__(self , Name, Type):
      self.Name = Name
      self.Type = Type

Animal1 = Pet("Alex", "dog")
Animal2 = Pet("Katty", "Cat")
Animal3 = Pet("Marco", "Bird")

print(Animal1.Name)
print(Animal1.Type)
print(Animal1.age)

print(Animal2.Name)
print(Animal2.Type)
print(Animal2.age)

print(Animal3.Name)
print(Animal3.Type)
print(Animal3.age)

# Challenge 3
# Book

class Book:
   def __init__(self, Title, Author, Pages):
      self.Title = Title
      self.Auther = Author
      self.Pages = Pages

Book1 = Book("Dopamine Nation", "Anna Lembke, MD", 304 )
Book2 = Book("Clear Thinking", "Shane Parrish", 288 )
Book3 = Book("Good to Great", "James C. Collins", 320 )

print(f"Title: {Book1.Title}")
print(f"Auther: {Book1.Auther}")
print(f"Pages: {Book1.Pages}")

print(f"Title: {Book2.Title}")
print(f"Auther: {Book2.Auther}")
print(f"Pages: {Book2.Pages}")

print(f"Title: {Book3.Title}")
print(f"Auther: {Book3.Auther}")
print(f"Pages: {Book3.Pages}")


# Challenge 4
# Character

class Character:
   Health = 100
   Attack = 100
   def __init__(self, Name, Attack):
      self.Name = Name

Knight = Character("Knight")
Wizard = Character("Wizard")

print(Knight.Name)
print(Knight.Health)
print(Knight.Attack)

print(Wizard.Name)
print(Wizard.Health)
print(Wizard.Attack)


# Challenge 5
# Garage

class Car:
   def __init__(self, Model, Year, Color):
      self.Model = Model
      self.Year = Year
      self.Color = Color

car1 = Car("Acura Integra", 2026, "Blue")
car2 = Car("Audi A4", 2025, "Black")
car3 = Car("BMW 3-Series", 2026, "Blue")


car1.Color = "Red"

print(car1.Model)
print(car1.Year)
print(car1.Color)

print(car2.Model)
print(car2.Year)
print(car2.Color)

print(car3.Model)
print(car3.Year)
print(car3.Color)


class Dog:
   def bark():
     print("Woof Woof!")

dog1 = Dog()
dog1.bark()


# Inheritance

class Animals:
   def __init__(self, Name, Color, Type):
      self.Name = Name
      self.Color = Color
      self.Type = Type

   def Sleeping(self):
      print(f"{Animals.Name} is Sleeping")   

   def Eating(self):
      print(f"{Animals.Name} is Eating")


class Cats(Animals):
   def __init__(self, Name, Color, Type, Food, Alive):
      super().__init__(Name, Color, Type)
      self.Food = Food
      self.Alive = Alive

class Dogs(Animals):
   def __init__(self, Name, Color, Type, Health, Runing):
      super().__init__(Name, Color, Type)
      self.Health = Health
      self.Runing = Runing

class Birds(Animals):
   def __init__(self, Name, Color, Type, Fly, Eggs):
      super().__init__(Name, Color, Type)
      self.Fly = Fly
      self.Eggs = Eggs

cat1 = Cats("Alex", "Blue", "Cat", "Fish", True)
Dog1 = Dogs("Rex", "Black", "Dog", "Good", False)
Bird1 = Birds("Koko", "Red", "Bird", True, False)

print(cat1.Name)
print(cat1.Color)
print(cat1.Type)
print(cat1.Food)
print(cat1.Alive) 

print(Dog1.Name)
print(Dog1.Color)
print(Dog1.Type)
print(Dog1.Health)
print(Dog1.Runing) 

print(Bird1.Name)
print(Bird1.Color)
print(Bird1.Type)
print(Bird1.Fly)
print(Bird1.Eggs) 