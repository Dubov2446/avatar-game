"""
File: avatar.py

Author: Josue Lopez

Course/Class and section: CS302-002

Date: 2nd December 2023

Program: CS302-002-program4/5

Description: File that contains the class hierarchy as well as its implementation.
             currently there is 1 Base class with 3 derieved sub classes that all
             stem from the Base. Everything related to the class hierarchy is 
             confined to this file. 

****************************** BASE CLASS *************************************
class Avatar:
  def __init__(self):
    - How to use: You would use this to create a new object of type Avatar, doing
      this will set the instance(s) variable(s) to some default value. They can be
      accessed and modified through other member methods. No return value.

    - example call: obj = Avatar()

    - How to maintain: You do not have to change this unless you plan to change the 
      instance variable(s), add any more, or delete any. Doing so will incur changes
      to the entirety hierarchy, so you most likely need to update every other sub class
      that steams from this class. 

  def increase_level(self):
    - How to use: You would use this to increase the value of the instance variable
      inside the class. No return value.

    - example call: obj.increase_level()

    - How to maintain: You do not have to change this unless you plan to change the 
      instance variable inside the class. Otherwise, no action is needed right now.

  def decrease_level(self):
    - How to use: You would use this to decrease the value of the instance variable
      inside the class. No return value.

    - example call: obj.decrease_level()

    - How to maintain: You do not have to change this unless you plan to change the 
      instance variable inside the class. Otherwise, no action is needed right now.

  def get_level(self):
    - How to use: You would use this to get the value of the instance variable
      inside the class. Returns its information unmanipulated.

    - example call: print(obj.get_level()) or catch_value = obj.get_level()

    - How to maintain: You do not have to do anything right now, however, 
      if you do decide to change the instance variable in anyway, you 
      need to update the class funcitons/variables that rely on things you've 
      changed. No action is needed as of now. 

****************************** MARKSMAN CLASS *************************************

class Marksman(Avatar):
  def __init__(self):
    - How to use: You would use this to create a new object of type Marksman, doing
      this will set the instance(s) variable(s) to some default value as well as setting
      up the base class constructor. They can be accessed and modified through other 
      member methods. No return value.

    - example call: obj = Marksman()

    - How to maintain: You do not have to change this unless you plan to change the 
      instance variable(s), add any more, or delete any. Doing so will incur changes
      to the entirety of class, so you most likely need to update every other method 
      that steams from within this class. 

  def delete_person(self):
    - How to use: You would use this to increase the value of the instance variable
      inside the class. No return value.

    - example call: obj.delete_person()

    - How to maintain: You do not have to change this unless you plan to change the 
      instance variable inside the class. Otherwise, no action is needed right now.

  def amount_of_people_deleted(self):
    - How to use: You would use this to get the value of the instance variable
      inside the class. Returns its information unmanipulated.

    - example call: print(obj.amount_of_people_deleted()) or catch = obj.amount_of_people_deleted()

    - How to maintain: You do not have to do anything right now, however, if you 
      do decide to change the instance variable in anyway, you need to update the 
      class funcitons/variables that rely on things you've changed. No action is needed as of now. 

  def play(self):
    - How to use: You would use this from the red-black binary tree class, as that is 
      where this method is called from when the user gets prompted to continue playing
      as an existing avatar. Will send the user to the class game until they decide to 
      exit. No return value returned.

    - example call: obj.play()

    - How to maintain: You do not have to do anything right now, however, if you 
      do decide to change the game in anyway, you need to update the 
      class funcitons/variables that rely on things you've changed. No action is needed as of now. 

****************************** ENGINEER CLASS *************************************

class Engineer(Avatar):
  def __init__(self):
    - How to use: You would use this to create a new object of type Engineer, doing
      this will set the instance(s) variable(s) to some default value as well as setting
      up the base class constructor. They can be accessed and modified through other 
      member methods. No return value.

    - example call: obj = Engineer()

    - How to maintain: You do not have to change this unless you plan to change the 
      instance variable(s), add any more, or delete any. Doing so will incur changes
      to the entirety of the class, so you most likely need to update every other method 
      that steams from within this class. 

  def fix_item(self):
    - How to use: You would use this to increase the value of the instance variable
      inside the class. No return value.

    - example call: obj.fix_item()

    - How to maintain: You do not have to change this unless you plan to change the 
      instance variable inside the class. Otherwise, no action is needed right now.

  def amount_of_items_fixed(self):
    - How to use: You would use this to get the value of the instance variable
      inside the class. Returns its information unmanipulated.

    - example call: print(obj.amount_of_items_fixed()) or catch = obj.amount_of_items_fixed()

    - How to maintain: You do not have to do anything right now, however, if you 
      do decide to change the instance variable in anyway, you need to update the 
      class funcitons/variables that rely on things you've changed. No action is needed as of now. 
  
  def play(self):
    - How to use: You would use this from the red-black binary tree class, as that is 
      where this method is called from when the user gets prompted to continue playing
      as an existing avatar. Will send the user to the class game until they decide to 
      exit. No return value returned.

    - example call: obj.play()

    - How to maintain: You do not have to do anything right now, however, if you 
      do decide to change the game in anyway, you need to update the 
      class funcitons/variables that rely on things you've changed. No action is needed as of now. 

****************************** MEDIC CLASS *************************************

class Medic(Avatar):
  def __init__(self):
    - How to use: You would use this to create a new object of type Medic, doing
      this will set the instance(s) variable(s) to some default value as well as setting
      up the base class constructor. They can be accessed and modified through other 
      member methods. No return value.

    - example call: obj = Medic()

    - How to maintain: You do not have to change this unless you plan to change the 
      instance variable(s), add any more, or delete any. Doing so will incur changes
      to the entirety of the class, so you most likely need to update every other method 
      that steams from within this class. 

  def heal_person(self):
    - How to use: You would use this to increase the value of the instance variable
      inside the class. No return value.

    - example call: obj.heal_person()

    - How to maintain: You do not have to change this unless you plan to change the 
      instance variable inside the class. Otherwise, no action is needed right now.

  def amount_of_people_healed(self):
    - How to use: You would use this to get the value of the instance variable
      inside the class. Returns its information unmanipulated.

    - example call: print(obj.amount_of_people_healed()) or catch = obj.amount_of_people_healed()

    - How to maintain: You do not have to do anything right now, however, if you 
      do decide to change the instance variable in anyway, you need to update the 
      class funcitons/variables that rely on things you've changed. No action is needed as of now. 

  def play(self):
    - How to use: You would use this from the red-black binary tree class, as that is 
      where this method is called from when the user gets prompted to continue playing
      as an existing avatar. Will send the user to the class game until they decide to 
      exit. No return value returned.

    - example call: obj.play()

    - How to maintain: You do not have to do anything right now, however, if you 
      do decide to change the game in anyway, you need to update the 
      class funcitons/variables that rely on things you've changed. No action is needed as of now. 
"""
import random
import numpy as np

class Avatar: # BASE CLASS
  def __init__(self):
    self._level = 0 # all characters start off at lvl zero

  # LEVEL STUFF
  def increase_level(self):
    self._level += 1
  def decrease_level(self):
    self._level -= 1
  def get_level(self):
    return self._level

class Marksman(Avatar):
  def __init__(self):
    super().__init__()
    # MARKSMAN PROTECTED MEMBERS
    self._people_deleted = 0 # you just started 

  def delete_person(self):
    self._people_deleted += 1 # you've deleted another person

  def amount_of_people_deleted(self):
    return self._people_deleted

  def play(self):
    string_array = np.array(["OPEN YOUR EYES???", "Terrible shot..", "so bad...", "WHAT??", "lol?"])

    user_choice = -1

    while user_choice != 0:
      if super().get_level() == 100:
        print("Congrats you reached lvl 100, you did so good omg yay!!")
      print("\n\n0 - abandon mission and return home....")
      print("1 - see level")
      print("2 - use crossbow!")
      print("3 - use sniper rifle!")
      print("4 - you're out of ammo, BUT THERE'S A ROCK????? THROW IT????")
      print("5 - see how many people you've deleted\n\n")

      user_choice = input("Enter your next move! ")

      try:
        user_choice = int(user_choice)
        if int(user_choice) < 0 or int(user_choice) > 5:
          raise ValueError

        if user_choice == 0:
          print("\nNo worries, head back to homebase and rest....")

        elif user_choice == 1:
          print(f"\nYour level: {super().get_level()}")

        # if you miss a shot, you lose a level
        elif user_choice == 2 or user_choice == 3 or user_choice == 4:
          if random.randint(1, 4) == 4: #  
            print(f"MISSED YOUR SHOT, {str(np.random.choice(string_array))}")
            if super().get_level() != 0:
              super().decrease_level()
          else:
            self.delete_person()
            super().increase_level()
            print("\nPERSON DELETED!")

        elif user_choice == 5:
          print(f"\nYou've deleted: {self.amount_of_people_deleted()} people\n")
      except Exception as err:
        print("Invalid input, try again...\n")



class Engineer(Avatar):
  def __init__(self):
    super().__init__()
    self._items_fixed = 0

  def fix_item(self):
    self._items_fixed += 1

  def amount_of_items_fixed(self):
    return self._items_fixed
  
  def play(self):
    string_array = np.array(["shocked yourself? haha", "wrong tool...", "so bad...", "lol?"])

    user_choice = -1

    while user_choice != 0:
      if super().get_level() == 100:
        print("Congrats you reached lvl 100, you did so good omg yay!!")
      print("\n\n0 - abandon mission and return home....")
      print("1 - see level")
      print("2 - use a screwdriver!")
      print("3 - use some tape!")
      print("4 - you're out of tape, BUT THERE'S ANIMAL WAX????? IT SHOULD WORK?")
      print("5 - see how many items you've fixed\n\n")

      user_choice = input("Enter your next move! ")

      try:
        user_choice = int(user_choice)
        if int(user_choice) < 0 or int(user_choice) > 5:
          raise ValueError

        if user_choice == 0:
          print("\nNo worries, head back to homebase and rest....")

        elif user_choice == 1:
          print(f"\nYour level: {super().get_level()}")

        # if you miss a shot, you lose a level
        elif user_choice == 2 or user_choice == 3 or user_choice == 4:
          if random.randint(1, 4) == 4: #  
            print(f"REPAIR FAILED! ITEM STILL BROKEN, {str(np.random.choice(string_array))}")
            if super().get_level() != 0:
              super().decrease_level()
          else:
            self.fix_item()
            super().increase_level()
            print("\nITEM FIXED!")

        elif user_choice == 5:
          print(f"\nYou've fixed: {self.amount_of_items_fixed()} items!\n")
      except Exception as err:
        print("Invalid input, try again...\n")

class Medic(Avatar):
  def __init__(self):
    super().__init__()
    self._people_healed = 0

  def heal_person(self):
    self._people_healed += 1

  def amount_of_people_healed(self):
    return self._people_healed

  def play(self):
    string_array = np.array(["PATIENT IS BLEEDING!!", "STITCH CAME UNDONE!", 
                            "PATIENT IS HAVING A SEIZURE", "BRAIN IS SWELLING"])

    user_choice = -1

    while user_choice != 0:
      if super().get_level() == 100:
        print("Congrats you reached lvl 100, you did so good omg yay!!")
      print("\n\n0 - abandon mission and return home....")
      print("1 - see level")
      print("2 - use SCALPAL!")
      print("3 - use FORCEPS!")
      print("4 - BRAIN IS SWELLING! PERFORM A CRANIECTOMY!!!")
      print("5 - see how many people you've saved\n\n")

      user_choice = input("Enter your next move! ")

      try:
        user_choice = int(user_choice)
        if int(user_choice) < 0 or int(user_choice) > 5:
          raise ValueError

        if user_choice == 0:
          print("\nNo worries, head back to homebase and rest....")

        elif user_choice == 1:
          print(f"\nYour level: {super().get_level()}")

        # if you miss a shot, you lose a level
        elif user_choice == 2 or user_choice == 3 or user_choice == 4:
          if random.randint(1, 4) == 4: #  
            print(f"SURGERY FAILED!, {str(np.random.choice(string_array))}")
            if super().get_level() != 0:
              super().decrease_level()
          else:
            self.heal_person()
            super().increase_level()
            print("\nPERSON HEALED AND SAVED!!!!!!")

        elif user_choice == 5:
          print(f"\nYou've healed: {self.amount_of_people_healed()} PEOPLE!\n")
      except Exception as err:
        print("Invalid input, try again...\n")