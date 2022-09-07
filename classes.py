class Person:
    # self verwys na hele ding en dit moet altyd eerste parameter wees
    def __init__(self, age, weight, height, first_name, last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name

user = Person(25, 80, 177, "Persoon", "White") # default python constructer word hier gebruik

print(user.last_name)