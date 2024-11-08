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

  def set_make(self,make):
    self.__make=make
  
  def set_model(self,year_model):
    self.__year_model=year_model
  
  def set_speed(self,speed):
    self.__speed=speed
  
  def get_make(self):
    return self.make
   
  def get_model(self):
    return self.year_model
  
  def get_speed(self):
    return self.speed
   
  def accelerate(self,speed):
    speed=int(speed)+5
    
  def brake(self,speed):
    speed=int(speed)-5

car_data=Car("McLaren F1 LM","1996",0) 

def main():
  for x in range(5):
    car_data.accelerate(speed)
    print('Current speed is: ', speed.get_speed(),'mph')
  for x in range(5):
    speed.brake()
    print('Current speed is: ', speed.get_speed(),'mph')

main()
