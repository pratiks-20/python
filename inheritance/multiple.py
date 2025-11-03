class vehicle:
    def move(self):
        print("vehicle moves")

class car(vehicle):
    def drive(self):
        print("car drives")

class boat(vehicle):
    def sail(self):
        print("boat sails")

class multiple(car, boat):
    pass

a = multiple()
a.move()
a.drive()
a.sail()
