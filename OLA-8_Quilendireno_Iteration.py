# MACHINE PROBLEM :
#1. Write a program that will accept words and store it in a list, a word bank.
#2. The program will ask the user to enter a word.
#3. The program will store the word in a list.
#4. The program will ask the user if he wants to try again. The user will input Y or y for yes, and N or n for no.
#5. If yes, refer to step 2.
#6. If no, display the total number of words and all the words that the user entered.

word_bank = []

while True:
    word = input("Enter a word: ")
    print(f"You entered the word {word}.")
    word_bank.append(word)

    again = input("Do you want to try again? [Y/N] ").strip().lower()
    if again == "n":
        break

print(f"\nYou entered {len(word_bank)} words:")
for word in word_bank:
    print(word)