from abc import ABC, abstractmethod

class Animal(ABC):
  @abstractmethod
  def sound(self):
    pass
  def sleep(self):
    print("Animal is sleeping")

class Cat(Animal):
  def sound(self):
    print("Meow")
  
class Cow(Animal):
  def sound(self):
    print("Moo")

c=Cat()
c.sound()
c.sleep()

cow=Cow()
cow.sound()
cow.sleep()
