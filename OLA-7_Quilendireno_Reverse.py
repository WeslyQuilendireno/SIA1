# MACHINE PROBLEM:
#1. Create a Python program that reverses a string.
#2. The user will input a word or words.
#3. Create a function that will reverse the string input and capitalize each letter.
#4. Display the original word, reversed word, and element count.

def reverse_string(text):
    reversed_text = text[::-1].upper()
    return reversed_text

word = input("Enter word/s: ")

reversed_word = reverse_string(word)
char_count = len(word)

print(f"STRING: {word}")
print(f"REVERSED: {reversed_word} ({char_count} characters)")