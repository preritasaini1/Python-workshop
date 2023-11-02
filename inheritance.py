#inheritance-allows you to create new classes that inherit properties and methods from existing classes

class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class dog(animal):    #using classes in differnt class....
    def speak(self):
        return "woof!"
class cat(animal):
    def speak(self):
        return "meow!"
dog1=dog("buddy")
cat1=cat("whiskers")
print(dog1.name,dog1.speak())
print(cat1.name,cat1.speak())