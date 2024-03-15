"""
File: game.py

Author: Josue Lopez

Course/Class and section: CS302-002

Date: 2nd December 2023

Program: CS302-002-program4/5

Description: File for the Game class and it also serves as the 
             implementation file for the class. All related
             class information regarding this class will be contained to 
             the contents of this file. 

def __init__(self):
  - How to use: You would use this to create a new object of type Game, doing
    this will set the instance(s) variable(s) to some default value. They can be
    accessed and modified through other member methods. No return value.

  - example call: obj = Game()

  - How to maintain: You do not have to change this unless you plan to change the 
    instance variable(s), add any more, or delete any. Doing so will incur changes
    to the entirety of the class, so you most likely need to update every other 
    method that steams from this class. 

def buy_item(self, item):
  - How to use: You would use this to add an item to the list that is
    located in the class constructor. will keep track of all your bought items
    and keep stored. Item you want to buy will be the argument and it will be 
    appended to the list. No return value.

  - example call: self.buy_item(user_item)

  - How to maintain: You do not have to change this unless you plan to change the 
    list in anyway whatsoever. Doing so will incur changes to the entirety 
    of the class, so you most likely need to update every other method that 
    steams from this class. 

def show_items(self):
  - How to use: You would use this to show the item(s) in the list,
    it will keep track of all your bought items. Item you want to buy 
    will be the argument to the method and it will be appended to the list.
    No return value.

  - example call: self.show_items()

  - How to maintain: You do not have to change this unless you plan to change the 
    list in anyway whatsoever. Doing so will incur changes to the entirety 
    of the class, so you most likely need to update every other method that 
    steams from this class. 

def menu(self):
  - How to use: You would use this to display the game menu to the user. This
    method is a read-only, as it only prints the menu and does not handle input
    in any manner. You would only use this when/where you want the menu to the game
    to be displayed. No return value.

  - example call: self.menu()
  
  - How to maintain: You do not have to maintain this in anyway as it only prints.
    However, if you plan to change the game in anyway, you must update the menu 
    to align with changes you've made. Otherwise no action is needed.

def play(self):
  - How to use: You would use this to invoke a play session in the main profile
    for the user to choose from. This is the "main" method that the game class
    centers around as it uses a Tree object to store the data of the user, 
    allowing them to enter in new information and refer back to previously 
    entered information so that they can keep playing as a avatar they
    entered some time in the past. You can think of this as "home base" in a
    sense and the starting point for a new game session. 

  - example call: user.play()

  - How to maintain: Since this is the main method that the game relies on, 
    maintaining this will be of utmost importance. Any changes you plan to
    make to the game in anyway whatsoever, will unquestionably incur changes 
    to the entirety of the class, so you most likely need to update every 
    other method that steams from this class. However, as of now you do
    not need to take any action. 
"""

from rbtree import *

class Game:
  def __init__(self):
    self._items = []

  def buy_item(self, item):
    self._items.append(item)

  def show_items(self):
    print("\nItems: ")
    for item in range(len(self._items)):
      print(self._items[item])

  def menu(self):
    print("\nWillkommen zurück! You're currently in your main profile btw")
    print("0 - quit")
    print("1 - add new character")
    print("2 - continue existing game with existing character")
    print("3 - display all saved characters")
    print("4 - buy any item you want")
    print("5 - show bought items\n")

  def play(self):
    choice = -1
    my_game = Tree()
    user_name = ""
    user_item = ""

    while choice != 0:
      print("\n")
      self.menu()
      
      choice = input("Enter choice: ")

      try:
        choice = int(choice)
        if int(choice) < 0 or int(choice) > 5:
          raise ValueError

        if choice == 1:
          user_name = input("Enter in username: ")
          character_choice = -1

          while character_choice < 1 or character_choice > 3:
            print("\n1 - Marksman")
            print("2 - Engineeer")
            print("3 - Medic")
            character_choice = input("Enter charactor you'd like to play as: ")

            try:
              character_choice = int(character_choice)
              if character_choice < 1 or character_choice > 3:
                raise ValueError
            except Exception as err:
              print("Try again, not a valid character...\n")
              character_choice = -1
            else:
              print("\n")
              if my_game.insert(user_name, character_choice) == True:
                print(f"{user_name} entered! ")
                character_choice = 1
              else:
                print(f"{user_name} has already been entered...")
                character_choice = 1
        
        elif choice == 2:
          user_name = input("Enter username to continue playing as: ")
          
          print("\n")
          if(my_game.search(user_name) == False):
            print(f"Sorry, cannot find match for: {user_name}")
          else:
            my_game.keep_playing(user_name)

        elif choice == 3:
          print("\n")
          my_game.inorder()

        elif choice == 4:
          user_item = input("Enter item to buy: ")
          if len(user_item) == 0:
            print("\nNo input was entered....")
          else:
            print("\n")
            self.buy_item(user_item)

        elif choice == 5:
          print("\n")
          self.show_items()

      except Exception as err: # catches all wrong input
        print("Invalid entry, try again...\n")