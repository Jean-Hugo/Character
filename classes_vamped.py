"""This code file contains code that guides the users on a person"""
class Person:
    id:str = None
    name:str = None
    surname:str = None
    balance:float = None

    def __init__(self, name, surname, *args, **kwargs) -> None:
        self.name = name
        self.surname = surname

def print_name(person:Person):
    print(person.name, person.surname)    

def read_file(filename:str):
    """This function reads the names_list.txt"""
    names_list = []
    file = open(filename, "r+", encoding="UTF-8")
    for line in file.readlines():
        names_list.append(line)
    return names_list

#person1 = Person("Skuld", "November")
#print_name(person1)

raw_people_data = read_file("names_list.txt")