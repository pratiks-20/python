class animal:
    def sound(self):
        print("animals make different sounds")
    class dog (animal):
        def sound(self):
            print("dog barks")

    d=dog()
    d.sound()
