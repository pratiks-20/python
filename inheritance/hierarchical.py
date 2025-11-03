class vehicle:
    def start(self):
        print("vehicle started")

class car(vehicle):
    def drive(self):
        print("car is driving")

class bike(vehicle):
    def ride(self):
        print("bike is riding")

class truck(vehicle):
    def load(self):
        print("truck is loading cargo")

c = car()
c.start()
c.drive()

b = bike()
b.start()
b.ride()

t = truck()
t.start()
t.load()
