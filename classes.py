class Person:
    # self verwys na hele ding en dit moet altyd eerste parameter wees
    def __init__(self, age, weight, height, first_name, last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name

    def information(self):
        print("Ek is " + str(self.age) + " jaar oud")
        print("Ek weeg " + str(self.weight) + " kg")
        print("Ek is " + str(self.height) + "cm lank")
        print("My naam is " + self.first_name)
        print("My van is " + self.last_name)

user = Person(25, 80, 177, "Persoon", "White") # default python constructer word hier gebruik

user.information()