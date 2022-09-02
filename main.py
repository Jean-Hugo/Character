"""This is the code file that contains the main functions
# Finding characters in strings
"""
valid_sentences_list:list = []

def find_character(supply_character:str, supply_sentence:str):
    """A functions that will try and find the character in the sentence.
    # Returns True if found
    # Rerturns False if not found"""
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

def get_supply_sentence()->str:
    """Function dedicated to getting supplied sentence"""
    return input("Supply your sentence: ")

def get_valid_sentence(the_char:str)->str:
    """A sentence that contains the character the user inserted"""
    the_sentence = get_supply_sentence()
    if find_character(the_char, the_sentence):
        return the_sentence
    return get_valid_sentence(the_char)

def add_to_list(vaild_sentice:str):
    """This function adds the sentence to the global valid_sentences_list"""
    # TODO add senteces to list
    return

def display_list():
    """Function that displays the global valid_sentences_list"""
    # TODO print sentences in one by one in a loop. 
    return
    
def main():
    """Produces a list of valid sentences"""
    while True:
        the_char = get_supply_character()
        the_valid_sentence = get_valid_sentence(the_char)
        add_to_list(the_valid_sentence) # TODO remember
        print("Your valid sentence is \n" + the_valid_sentence)
        another = input("Whould you like to try another?(Y/N) ")
        if "Y" in another:
            continue
        elif "N" in another:
            print("Thank you for using this program. Arigato gozaimasu")
            display_list() # TODO remeber
            break
        else:
            print("Idiot! Y or N. \nSuffer another round!")
            continue

main()