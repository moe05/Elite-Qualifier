import unittest
import sys
import random


#Added this as a simple "Get to know the user feature"
print("Hello! Im ChatterBot, what is your name?")
user_input= input()
print(f"Nice to meet you {user_input}!")
print("Where are you from?")
user_input = input()
print(f"I've heard {user_input} is a very nice place.")
print("Lets get Talking!:)")
input()

def words (user_input):
  sayings = [
    "Really?",
    "OUTRAGEOUS!", 
    "Ok.", 
    "mmhmmmm.", 
    "Ugh, gag me with a spoon!", 
    "As if!", 
    "How Bri'ish", 
    "so?"
    ]
  return random.choice(sayings)



while True: #This is used as a main loop for the program
 user_input = input(words(user_input) + "\n")
 if user_input == "bye":
  print("Mr. Stark I dont feel so good.....")
  sys.exit()










