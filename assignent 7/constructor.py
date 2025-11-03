class student:
    def __init__(self,name,age):
            self.name=name
            self.age=age
            print("Constructor is called!")
s1=student("pratik",16)
print("name :",s1.name)
print("age :",s1.age)