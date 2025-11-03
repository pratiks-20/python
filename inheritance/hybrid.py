class vehicle:
    def start(self):
        print("vehicle started")

class car(vehicle):
    def drive(self):
        print("car drives")

class electric(vehicle):
    def charge(self):
        print("charging")

class hybrid_car(car, electric):
    def eco(self):
        print("hybrid car in eco mode")

hc = hybrid_car()
hc.start()
hc.drive()
hc.charge()
hc.eco()
