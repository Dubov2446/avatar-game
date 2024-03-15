"""
File: main.py

Author: Josue Lopez

Course/Class and section: CS302-002

Date: 2nd December 2023

Program: CS302-002-program4/5

Description: File for the main function/user interface. Also used to
             provide the introduction instructions, as well as the 
             ending goodbye message. This will serve as the file
             to be ran. It will create a game and a user
             experience.

def instructions():
    - how to use: You would use this in the same manner as any other void function
      and it will output a greeding message that also explains how the game
      works. There is no return type.

    - example call: instructions()

    - how to maintain: You do not need to do anything to maintain this as it
      only contains print functions. If you wish to change the game, make sure
      to update the instructions to align with the made changes. Otherwise, no
      action is needed right now. 

def goodbye_message():
    - how to use: You would use this in the same manner as any other void function
      and it will output an ending message with a poem. There is no return type.

    - example call: goodbye_message()

    - how to maintain: You do not need to do anything to maintain this as it
      only contains print functions. If you wish to change the game, make sure
      to update the message to align with the made changes. Otherwise, no
      action is needed right now. 
"""
from game import *

def instructions():
  print("\n\nINSTRUCTIONS FOR HOW TO PLAY, PAY ATTENTION!!!!!")
  print("You have a main profile and you can set up mini profiles")
  print("to have mulitple avatars that you can play from!")
  print("In your main profile you can buy items, see what items you've bought")
  print("and choose what character you want to play as or CREATE A NEW ONE! YAY!!")
  print("You cannot create duplicate characters with the same name")
  print("and each character has unique abilites/powers")
  print("THAT'S ALL FOLKS! TRY AND REACH LEVEL 100 IF YOU CAN FOR A PRIZE!\n")

def goodbye_message():
  print("\n\nThanks for playing! Have a splendid and fulfilled day with nothing but goodness!")
  print("And to make that come true, here's a poem FOR YOU!!!!\n\n")
  print("In the realm of codes and circuits bright,")
  print("I navigate the digital sea with delight.")
  print("A computer science student, full of glee,")
  print("In a world of algorithms, wild and free.\n")
  print("Binary ballet, zeros and ones,")
  print("Dancing together, having tons of fun.")
  print("Syntax errors sneak, like mischievous sprites,")
  print("But I conquer them all, through many late nights.\n")
  print("I speak in languages strange and grand,")
  print("Python, Java, and C++ at my command.")
  print("I ponder in loops, in recursive dreams,")
  print("Where algorithms flow in logical streams.\n")
  print("In the ciphered gardens of data, where bytes do bloom")
  print("The scholar tends to algorithms, dispelling the gloom")
  print("In the court of computation, where knowledge holds the key,")
  print("A symphony of circuits, a marvel to decree\n")
  print("A debugger's my sidekick, a trusty guide,")
  print("Through the realms of logic, far and wide.")
  print("In the kingdom of bytes, where data resides,")
  print("I seek patterns, like digital tides.")
  print("In the whimsical world of codes and schemes,")
  print("I'm just a computer science student, living the dream.\n\n")

def main(): # GAME STARTS FROM THIS FILE/FUNCTION. PLAY HERE!!!!!
  # user is kick started to play a new game
  # given options via menu function
  instructions()
  user = Game()
  user.play()
  goodbye_message()

if __name__ == "__main__":
  main()