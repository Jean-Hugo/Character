class Person:
    def self(self, age, weight, height, first_name, last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        print("my naam is " + user.first_name + " " + user.last_name)
        print("My gewig is " + str(user.weight))
        print("My lengte is " + str(user.height))

user = Person() # default python constructer word hier gebruik
user.age = 25
user.weight = 80
user.height = 177
user.first_name = "Persoon"
user.last_name = "White"

user.self()