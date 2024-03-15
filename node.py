"""
File: node.py

Author: Josue Lopez

Course/Class and section: CS302-002

Date: 2nd December 2023

Program: CS302-002-program4/5

Description: File for the node class, below has all the functions that are
            needed for a node that goes inside of a red-black binary search tree.
            Basic functions have been implemented and tested. If you plan to
            change anything, it would also be best to modify other files 
            since they depend on this specific implementation!

def __init__(self, data = None, color = 0, parent = None, left = None, right = None, player = None):
    - How to use: You would this function whenever you want to create a new "Node" object. You have
      the option to insert values into the Node to and by doing this you will set the default
      values for the Node to what you desire. If you choose to not do this, the Node values
      will be set by default leaving the Node variable "empty."

    - example call: obj = Node() or obj = Node(data, 1, None, self.NIL, self.NIL, user_choice)

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now. 

def play_avatar(self):
    - How to use: you call this whenever you're at a certain node and want to play as the
      character you have saved in that Node. This will intern call another function
      within the avatar class based off what the object is. 

    - example call: current.play_avatar()

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now. Note that this will call a function within the
      Avatar class, so if you change any functions in there, you need to make sure it does not
      impact the play_avatar() function, and if it does, you need to update this function 
      in the process to maintain compatibility. 

def get_data(self):
    - How to use: you call this whenever you're at a certain node and want to get the
      data you have saved in that Node. The return value will not be manipulated
      in the return process. 

    - example call: print(obj.get_data()) or catch_value = obj.get_data()

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now. 

def get_parent(self):
    - How to use: you call this whenever you're at a certain node and want to get the
      parent information you have saved in that Node. The return value will not be manipulated
      in the return process. 

    - example call: catch_value = obj.get_parent()

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now. 

def get_color(self):
    - How to use: you call this whenever you're at a certain node and want to get the
      color information you have saved in that Node. The return value will not be manipulated
      in the return process. 

    - example call: catch_value = obj.get_color()

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now.  

def get_left(self):
    - How to use: you call this whenever you're at a certain node and want to get the
      left link you have saved in that Node. The return value will not be manipulated
      in the return process. 

    - example call: obj.set_left(obj2.get_left())

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now.  

def get_right(self):
    - How to use: you call this whenever you're at a certain node and want to get the
      right link you have saved in that Node. The return value will not be manipulated
      in the return process. 

    - example call: obj.set_right(obj2.get_right())

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now.  

def set_data(self, value):
    - How to use: you call this whenever you're at a certain node and want to set the
      data information in that Node. There is no return value.

    - example call: obj.set_data(100)

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now.

def set_color(self, value):
    - How to use: you call this whenever you're at a certain node and want to set the
      color information in that Node. There is no return value.

    - example call: obj.set_color(0)

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now.

def set_parent(self, value):
    - How to use: you call this whenever you're at a certain node and want to set the
      parent information in that Node. There is no return value.

    - example call: obj.set_parent(obj2.get_right())

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now.

def set_left(self, link):
    - How to use: you call this whenever you're at a certain node and want to set the
      left link in that Node. There is no return value.

    - example call: obj.set_left(obj2.get_left())

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now.

def set_right(self, link):
    - How to use: you call this whenever you're at a certain node and want to set the
      right link in that Node. There is no return value.

    - example call: obj.set_right(obj2.get_right())

    - How to maintain: You do not have to do anything right now, however, if you do decide to change
      the Node in anyway, you need to update the funcitons/variables that rely on things you've 
      changed. No action is needed as of now.
"""
class Node:
    def __init__(self, data = None, color = 0, parent = None, left = None, right = None, player = None):
        self._data = data
        # 0 for black, 1 for red
        self._color = color  
        self._parent = parent
        self._left = left
        self._right = right
        self._player = player # this will be the Avatar they pick

    def play_avatar(self):
        self._player.play()

    # getters
    def get_data(self):
        return self._data

    def get_parent(self):
        return self._parent

    def get_color(self):
        return self._color

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    # setters
    def set_data(self, value):
        self._data = value

    def set_color(self, value):
        self._color = value

    def set_parent(self, value):
        self._parent = value

    def set_left(self, link):
        self._left = link

    def set_right(self, link):
        self._right = link