class student:
    def __init__(self, name):
        self.name = name
        print("object created for", self.name)

    def __del__(self):
        print("destructor is called, object deleted")

s1 = student("pratik")
del s1  
