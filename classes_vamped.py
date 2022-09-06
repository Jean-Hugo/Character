"""This code file contains code that guides the users on a person"""
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QGridLayout, QLineEdit

class Person:
    id:str = None
    name:str = None
    surname:str = None
    gender:str = None
    balance:float = None

    def __init__(self, name:str, surname:str, gender:str=None, *args, **kwargs) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.set_gender()
    
    def set_gender(self):
        """This sets the gender for the person"""
        man = ["♂️", "man", "m", "M", "MAN", "XY"]
        female = ["♀️", "female", "woman", "w", "W", "XX"]
        if self.gender in man:
            self.gender = "Man"
            return
        elif self.gender in female:
            self.gender = "Female"
            return
        self.gender = "Weirdo"
        return

def print_name(person:Person):
    print(person.name, person.surname)    

def read_file(filename:str):
    """This function reads the names_list.txt"""
    names_list = []
    file = open(filename, "r+", encoding="UTF-8", newline=None)
    for line in file.readlines():
        names_list.append(line.strip())
    return names_list

def get_split_person_details(person_details:str, split_char:str):
    """Returns a list from the person details supplied"""
    try:
        splitted_person_details = person_details.split(" ")
        # House keeping & Error catching & Quality check
        if len(splitted_person_details) > 2:
            return splitted_person_details
        raise Exception("Error with person details! Check file!")
    except Exception as e:
        print(e)
        return [person_details, "ERROR"]

def format_person_details(splitted_details:list, format:int=0):
    """This fucntion returns the person details in a list form so that the Person object can be created in
    the Person Class"""
    # SETTING FORMAT
    person_format = None
    format_0 = ("gender", "name", "surname")
    format_1 = ("name", "surname", "gender")
    if format == 0:
        person_format = format_0
    else:
        person_format = format_1
    # INDEXING CORRECTLY
    if person_format == format_0:
        return [splitted_details[1], splitted_details[2], splitted_details[0]]
    elif person_format == format_1:
        return splitted_details
    else:
        return splitted_details

def create_list(filename:str):
    """Creates the import list [list[list]]"""
    people_list = [] # The list that will be returned
    raw_people_data = read_file(filename) # Read in the person details
    for person in raw_people_data: # Loop through the person details
        split_details = get_split_person_details(person, " ") # Split the person details 
        formated_split_details = format_person_details(split_details, 0) # Put the details in the right order
        people_list.append(formated_split_details) # Add the details to the list // list of list
    return people_list

def search_people_in_database(person:str):
    """TODO Search peron in the databasee"""
    return

def main(filename:str):
    names = create_list(filename)
    if(input("Do you want to display?(Y/N)") == "Y"):
        while True:
            option = input("1.All\n2.Names Only\n3.Name + Gender\n")
            if option == "1":
                print_all = [print(name) for name in names] # One liner advance
                break
            elif option == "2":
                print_names_only = [print(name[0]) for name in names]
                break
            elif option == "3":
                print_names_gender = [print(name[0], name[2]) for name in names]
                break
            else:
                print("Invalid option. Try again\n")


main("names_list.txt")
