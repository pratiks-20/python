class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")


animal = Animal()
dog = Dog()


animal.speak()  
dog.speak()   

