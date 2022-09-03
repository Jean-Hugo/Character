"""The basic version of main"""
supply_character = input("Supply your character: ")
how_many_sentences = int(input("How many sentences do you want to add: "))
x = 1
y = 1
list_of_sentences = []

while x <= how_many_sentences:
    supply_sentence = input("Supply your sentences: ")
    if supply_character in supply_sentence:
        list_of_sentences.append(supply_sentence)
        x += 1
    else:
        print("Supply a valid sentence.")

print_or_no_print = input("Do you want to print your sentences(Y/N): ")


if "Y" in print_or_no_print:
    for i in range(how_many_sentences):
        print(list_of_sentences[i])

another_round = input("do you wanna go another round(Y/N): ")

while "Y" in another_round:
    if y <= 3:
        print("You are not allowed to go another round.")
    elif y == 4:
        print("STOP SAYING YES!!! YOU AREN'T ALLOWED TO GO ANOTHER ROUND!!!")
    elif y == 5:
        print("What did I just say.")
    elif y >= 6:
        print("Why don't you listen")
    another_round = input("do you wanna go another round(Y/N): ")
    y += 1

print("Thank you for wasting your time.")