#Object----
#1._init_ - special object  used to initialize the object(method)
#2.self - is a reference to the current instance of a class.(reference)
#we use self always within __init__(its compulsary).

#creating an object-
class Dog:
    def __init__ (self,name):
        self.name=name 
dog1 = Dog("buddy")
print(dog1.name)

#creating a class-
class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
car1=Car("totyota","camry")   #creating objects from the class
car2=Car("honda","civic")
print(car1.make,car1.model)
print(car2.make,car2.model)



