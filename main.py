"""This is the code file that contains the main functions
# Finding characters in strings
"""

def find_character(supply_character:str, supply_sentence:str):
    if supply_character in supply_sentence:
        print(supply_character + " was found in " + supply_sentence)
        return True
    print(supply_character + " could not be found in " + supply_sentence)
    return False

def get_supply_character():
    """Function dedicated to get supplied character
    >> return "character"""
    the_char = input("Supply your character: ")
    if the_char is "*":
        print("* is not allowed")
        return get_supply_character()
    return the_char

def get_supply_sentence():
    """Function dedicated to getting supplied sentence"""
    return input("Supply your sentence: ")

def get_valid_sentence(the_char:str):
    """A sentence that contains the character the user inserted"""
    the_sentence = get_supply_sentence()
    if find_character(the_char, the_sentence):
        return the_sentence
    return get_valid_sentence(the_char)
    
def main():
    print("Hello world")
    while True:
        the_char = get_supply_character()
        the_valid_sentence = get_valid_sentence(the_char)
        print("Your valid sentence is \n" + the_valid_sentence)
        another = input("Whould you like to try another?(Y/N) ")
        if "Y" in another:
            continue
        elif "N" in another:
            print("Thank you for using this program. Arigato gozaimasu")
            break
        else:
            print("Idiot! Y or N. \nSuffer another round!")

main()