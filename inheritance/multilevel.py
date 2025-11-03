
class vehicle:
    def start(self):
        print("vehicle started")

class car(vehicle):
    def drive(self):
        print("car is driving")
 

class sports_car(car):
    def turbo_boost(self):
        print("sports car turbo boost activated")
 

sc = sports_car()
sc.start()
sc.drive()
sc.turbo_boost()
