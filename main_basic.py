"""The basic version of main"""
supply_character = input("Supply your character: ")
supply_sentence = input("Supply your sentence: ")

if supply_character in supply_sentence:
    print(supply_character + " was found in " + supply_sentence)
else:
    print(supply_character + " was not found in " + supply_sentence)