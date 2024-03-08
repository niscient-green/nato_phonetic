# Convert a string into a NATO alphabet word list

# Import packages
import random
import pandas
from art import nato_flag

# Set globals
nato_alphabet_dict = {}


# Welcome user
def welcome_message():
    print(nato_flag)
    print("Welcome to the NATO Phonetic Alphabet Tutor.")
    print("Type 'exit' when you're done.")


# Create a list of the phonetic code words from a word that the user inputs.
# In this format: {"A": "Alfa", "B": "Bravo"}
def create_dict():
    nato_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
    global nato_alphabet_dict
    nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet_df.iterrows()}


# Check the user's input against the dictionary
def check_answer(letter, user_input):
    code = nato_alphabet_dict[letter]
    if code == user_input.title():
        print("Correct!")
    else:
        print(f"Sorry, wrong. The answer was {code}")


# Main program loop
welcome_message()
create_dict()
continue_loop = True
while continue_loop:
    # Get a random letter
    letter = random.choice(list(nato_alphabet_dict.keys()))

    # Check if user input was to exit
    user_input = input(f"What is the phonetic code for the letter {letter}: ")
    if user_input.lower() == "exit":
        continue_loop = False
    else:
        check_answer(letter, user_input)