# Program # 2: Car Class
# Write a class named Car that has the following data attributes:

# __year_model (for the car's year model)
# __make (for the make of the car)
# __speed (for the car's current speed)
# The Car class should have an __init__ method that accepts the car's year model and make as arguments.  These values should be assigned to the object's __year_model and __make data attributes.  It should also assign 0 to the __speed data attribute.

# The class should also have the following methods:

# The accelerate method should add 5 to the speed data attribute each time it it called.
# The brake method should subtract 5 from the speed data attribute each time it is called.
# The get_speed method should return the current speed.
# Next, design a program that creates a Car object then calls the accelerate method five times.  After each call to the accelerate method, get the current speed of the car and display it.  The call the brake method.  After each call to the brake method, get the current speed of the car and display it.
class Car:
  def __init__(self, make, year_model, speed):
    self.__make=make
    self.__year_model=year_model
    self.__speed=speed
    
  def set_make(self,__make):
    self.__make=__make
  
  def set_model(self,__year_model):
    self.__year_model=__year_model
  
  def set_speed(self,__speed):
    self.__speed=__speed
  
  def get_make(self):
    return self.__make
   
  def get_model(self):
    return self.__year_model
  
  def get_speed(self):
    return self.__speed
   
  def accelerate():
    speed=0
    for accelerate in range(5):
      speed=speed+5
      print(speed,'mph')
  accelerate()
  
  def brake():
    speed=25
    for brake in range(5):
      speed=speed-5
      print(speed,'mph')
  brake()

car_data=Car("McLaren F1 LM","1996",0) 
