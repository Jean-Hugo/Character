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

def build_the_window():
    """Creates the window"""
    window = QWidget()
    window.setWindowTitle("Our App")
    return window

def build_button(button_name="Button"):
    """Creates the button object"""
    button = QPushButton()
    button.setText(button_name)
    return button

def build_line_edit(placeholder_text="Uhm?"):
    """Creates the line edit object"""
    line_edit = QLineEdit()
    line_edit.setPlaceholderText(placeholder_text)
    return line_edit

def change_line_edit(the_line_edit:QLineEdit, text:str):
    """Changes the line edit text style"""
    the_line_edit.setText(text)
    the_line_edit.move(250, 250)
    font = the_line_edit.font() # made a copy of the current font 
    font.setPointSize(20) # Altering size
    font.setBold(True) # Making bold
    the_line_edit.setFont(font) # Replacing the original font
    the_line_edit.resize(the_line_edit.sizeHint())
    the_line_edit.setStyleSheet('color: red')
    return

def build_table(data_objects:list[object]=None):
    """Build table with objects"""
    if data_objects is None:
        data_objects = retrieve_person_objects()
    the_table = QTableWidget()
    table_headings = data_objects[0].__dict__.keys()
    the_table.setHorizontalHeaderLabels(table_headings)
    the_table.setRowCount(1)
    print(table_headings)
    return the_table
    

def ux_charcter():
    """GUI for the charcter and search program"""
    app = QApplication([])

    def window():# The window
        return build_the_window()

    def button(parent, text):# The build
        button = build_button()
        button.setParent(parent)
        button.setText(text)
        return button
    
    def lineEdit(parent, placetext): # The line edit 
        line_edit = build_line_edit(placetext)
        line_edit.setParent(parent)
        return line_edit
    
    def table(parent, dataobjects):
        table = build_table(dataobjects)
        table.setParent(parent)
    
    def setup_window(): # builds the layout
        push_me_button.show()
        push_me_button.move(30, 40)
        line_result.show()
        line_result.move(250, 250)
        display_window.show()
    
    def setup_actions(): # Sets up things that happen
        push_me_button.pressed.connect(lambda: change_line_edit(line_result, "You pushed the button!"))

    display_window = window()
    push_me_button = button(display_window, "Push me!")
    line_result = lineEdit(display_window, "I'm the placeholder text��")
    person_table = table(display_window, retrieve_person_objects("names_list.txt"))
    setup_window()
    setup_actions()
    app.exec_()

def get_person_object_list(loaded_person_details:list):
    """Returns a list of Person objects. Given the list of loaded person details"""
    person_objects_list = []
    for person in loaded_person_details:
        name = person[0]
        surname = person[1]
        gender = person[2]
        person_objects_list.append(Person(name=name, surname=surname, gender=gender))
    return person_objects_list


def terminal_ui(loaded_person_details):
    """The UI in the terminal/commandline"""
    if(input("Do you want to display?(Y/N)") == "Y"):
        while True:
            option = input("1.All\n2.Names Only\n3.Name + Gender\n")
            if option == "1":
                print_all = [print(name) for name in loaded_person_details] # One liner advance
                break
            elif option == "2":
                print_names_only = [print(name[0]) for name in loaded_person_details]
                break
            elif option == "3":
                print_names_gender = [print(name[0], name[2]) for name in loaded_person_details]
                break
            else:
                print("Invalid option. Try again\n")


def retrieve_person_objects(filename:str):
    loaded_person_details = create_list(filename)
    person_objects = get_person_object_list(loaded_person_details=loaded_person_details)
    return person_objects

def main():
    our_app = ux_charcter()


if __name__ == "__main__":
    main()


       


    


