<<<<<<< HEAD
# MACHINE PROBLEM:
#1. Ask the user to input 3 nouns and 3 adjectives.
#2. Look for your favorite song lyrics. Replace the nouns and adjectives in the song lyrics with the user's input.
#3. Display both the original song lyrics and replaced song lyrics (both the replaced nouns and adjectives must be in ALL CAPS).


intro = ("""Quilendireno, Wesly C.
2BSIT-5\n""")

print (intro)

print ("noun")
noun1 = input("Noun 1: ")
noun2 = input("Noun 2: ")
noun3 = input("Noun 3: ")

print ("\nadjecive")
adjective1 = input("Adjective 1: ").upper()
adjective2 = input("Adjective 2: ").upper()
adjective3 = input("Adjective 3: ").upper()

noun1, noun2, noun3 = noun1.upper(), noun2.upper(), noun3.upper()

print ("\noriginal songs")
lyrics = """Happy birthday to you,
Happy birthday to you,
Happy birthday dear friend,
Happy birthday to youuu!."""

replaced = f"""{adjective1} {noun1} to you,
{adjective2} {noun1} to you,
{adjective3} {noun1} dear {noun2},
{adjective1} {noun3} to you."""

print("\n--- original song ---\n ")
print(lyrics)

print("\n--- replaced song ---")
=======
# MACHINE PROBLEM:
#1. Ask the user to input 3 nouns and 3 adjectives.
#2. Look for your favorite song lyrics. Replace the nouns and adjectives in the song lyrics with the user's input.
#3. Display both the original song lyrics and replaced song lyrics (both the replaced nouns and adjectives must be in ALL CAPS).


intro = ("""Quilendireno, Wesly C.
2BSIT-5\n""")

print (intro)

print ("noun")
noun1 = input("Noun 1: ")
noun2 = input("Noun 2: ")
noun3 = input("Noun 3: ")

print ("\nadjecive")
adjective1 = input("Adjective 1: ").upper()
adjective2 = input("Adjective 2: ").upper()
adjective3 = input("Adjective 3: ").upper()

noun1, noun2, noun3 = noun1.upper(), noun2.upper(), noun3.upper()

print ("\noriginal songs")
lyrics = """Happy birthday to you,
Happy birthday to you,
Happy birthday dear friend,
Happy birthday to youuu!."""

replaced = f"""{adjective1} {noun1} to you,
{adjective2} {noun1} to you,
{adjective3} {noun1} dear {noun2},
{adjective1} {noun3} to you."""

print("\n--- original song ---\n ")
print(lyrics)

print("\n--- replaced song ---")
>>>>>>> 0e24f6a61b5ebe0de3ed9817783479a27d9c7133
print(replaced)