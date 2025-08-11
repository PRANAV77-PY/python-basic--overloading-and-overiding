class Animal:
    def sound(self):
        print("Some generic animal sound")

    
class Dog:
    def sound(self):    #overiding parent method
        print("Bark")


#Object
dog = Dog()
dog.sound()
