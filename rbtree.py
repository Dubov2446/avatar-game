"""
File: rbtree.py

Author: Josue Lopez

Course/Class and section: CS302-002

Date: 2nd December 2023

Program: CS302-002-program4/5

Description: File for the red-black binary search tree and it also 
             serves as the implementation file for the class. All related
             class information regarding this class will be contained to 
             the contents of this file. 

def __init__(self):
  - How to use: You would use this to create a new object of type Tree, doing
    this will set the instance(s) variable(s) to some default value. They can be
    accessed and modified through other member methods. No return value.

  - example call: obj = Tree()

  - How to maintain: You do not have to change this unless you plan to change the 
    instance variable(s), add any more, or delete any. Doing so will incur changes
    to the entirety hierarchy, so you most likely need to update every other sub class
    that steams from this class. 

def insert(self, data):
  - How to use: You would use this to insert a new value in the tree. Information
    will be recieved by the user. This method will call a recursive version of
    itself and return its value to the root. This will only occur if the value
    does not previously exist in the tree. User will be alerted if data item
    was entered into the tree without error.

  - example call: obj.insert("DANIIL DUBOV")

  - How to maintain: You do not have to change this unless you plan to change the 
    insert process in any way. Doing so will incur changes to the entirety of 
    the class, so you most likely need to update every other method that steams from this class. 

def insert_recursive(self, root, new_node):
  - How to use: You would use this to insert a new value in the tree. Information
    will be recieved by the user. This method is the recursive version and will
    insert the value. Will also evaluate the validity of the red-black tree and if
    need be will change the colors/order of the tree by invoking rotating methods
    Returns the 'link' recursively and returns it to the root

  - example call: self.root = self.insert_recursive(self.root, new_node)

  - How to maintain: You do not have to change this unless you plan to change the 
    insert process in any way. Doing so will incur changes to the entirety of 
    the class, so you most likely need to update every other method that steams from this class. 

def search(self, data):
  - How to use: You would use this to search for a value in the tree. Information
    will be recieved by the user. This method will call the recursive version and will
    search for the value. Returns a boolean value depending on if the data value
    was found while searching the tree.

  - example call: if self.search(data) == False:

  - How to maintain: You do not have to change this unless you plan to change the 
    searching process in any way. Doing so will incur changes to the entirety of 
    the class, so you most likely need to update every other method that steams from this class. 

def search_recursive(self, current, data):
  - How to use: You would use this to search for a value in the tree. Information
    will be recieved by the user. This method is the recursive version and will
    search for the value. Returns a boolean value to the calling non-recursive 
    version depending on if the data value was found while searching the tree.

  - example call: return self.search_recursive(self.root, data)

  - How to maintain: You do not have to change this unless you plan to change the 
    searching process in any way. Doing so will incur changes to the entirety of 
    the class, so you most likely need to update every other method that steams from this class. 

def keep_playing(self, data):
  - How to use: You would use this to search for a value in the tree that already exists
    and that the user wants to continue playing as. Information will be recieved by 
    the user. This method will call the recursive version and will search for the value. 
    No value is returned.

  - example call: obj.keep_playing(data):

  - How to maintain: You do not have to change this unless you plan to change the 
    searching process in any way. Doing so will incur changes to the entirety of 
    the class, so you most likely need to update every other method that steams from this class. 

def keep_playing_recursive(self, current, data):
  - How to use: You would use this to search for a value in the tree. Information
    will be recieved by the user. This method is the recursive version and will
    search for the value. No value is returned.

  - example call: self.keep_playing_recursive(current.get_left(), data)

  - How to maintain: You do not have to change this unless you plan to change the 
    searching process in any way. Doing so will incur changes to the entirety of 
    the class, so you most likely need to update every other method that steams from this class. 

def rotate_left(self, current_node):
  - How to use: You wouldn't use this outside the tree, only to be used by another
    method that's part of the tree. This would be used when you want to perform
    a left rotation to keep balance within the tree and to satisfy red-black tree
    properties. Returns a 'link' to reconnect the tree to the calling method. 

  - example call: root = self.rotate_left(left)

  - How to maintain: You do not have to change this unless you plan to change the 
    rotation process in any way. Doing so will incur changes to the entirety of 
    the class, so you most likely need to update every other method that steams from this class. 

def rotate_right(self, current_node):
  - How to use: You wouldn't use this outside the tree, only to be used by another
    method that's part of the tree. This would be used when you want to perform
    a right rotation to keep balance within the tree and to satisfy red-black tree
    properties. Returns a 'link' to reconnect the tree to the calling method. 

  - example call: root = self.rotate_right(right)

  - How to maintain: You do not have to change this unless you plan to change the 
    rotation process in any way. Doing so will incur changes to the entirety of 
    the class, so you most likely need to update every other method that steams from this class. 

def flip_colors(self, current_node):
  - How to use: You wouldn't use this outside the tree, only to be used by another
    method that's part of the tree. This would be used when you want to perform
    a color flip between nodes to keep balance within the tree and to satisfy red-black tree
    properties. Returns no value, just performs the swap. 

  - example call: self.flip_colors(root)

  - How to maintain: You do not have to change this unless you plan to change the 
    color assignment process in any way. Doing so will incur changes to the entirety of 
    the class, so you most likely need to update every other method that steams from this class. 

def inorder(self):
  - How to use: You would use this to print the names of your avatar profiles that you're
    playing as and have saved. Print traversal will be inorder. This method will call the 
    recursive version and will print the values from within that method. No value is returned.

  - example call: obj.inorder():

  - How to maintain: You do not have to change this unless you plan to change the 
    printing/traversal process in any way. Otherwise, no action is required right now.

def inorder_recursive(self, node):
  - How to use: You would use this to search for a value in the tree. Information
    will be recieved by the user. This method is the recursive version and will
    search for the value. No value is returned.

  - How to use: You would use this to print the names of your avatar profiles that you're
    playing as and have saved. Print traversal will be inorder. This method is the recursive
    version and print each avatar name value. No value is returned.

  - example call: self.inorder_recursive(self.root)

  - How to maintain: You do not have to change this unless you plan to change the 
    printing/traversal process in any way. Otherwise, no action is required right now.
"""
from node import *
from avatar import *

class Tree:
    def __init__(self):
      # values are set their defualts via Nojde contructor
      self.NIL = Node()
      self.root = self.NIL

    def insert(self, data, character_choice):
      if self.search(data) == False:

        if character_choice == 1:
          user_choice = Marksman()

        elif character_choice == 2:
          user_choice = Engineer()

        else: # character_choice == 3
          user_choice = Medic() 

        new_node = Node(data, 1, None, self.NIL, self.NIL, user_choice)
        self.root = self.insert_recursive(self.root, new_node)
        self.root.set_color(0)  # Ensure the root is black
        return True
      else:
        return False

    def insert_recursive(self, root, new_node):
      if root == self.NIL: 
        return new_node

      if new_node.get_data() < root.get_data():
        root.set_left(self.insert_recursive(root.get_left(), new_node))
        root.get_left().set_parent(root)
      else:
        root.set_right(self.insert_recursive(root.get_right(), new_node))
        root.get_right().set_parent(root)

      # checks for imbalance here to correct it
      # REMEMBER! black = 0 and red = 1
      # case where right is red and left is black
      if root.get_right().get_color() == 1 and root.get_left().get_color() == 0:
        root = self.rotate_left(root)

      # case where left is red and 2 to the left is also red
      if root.get_left().get_color() == 1 and root.get_left().get_left().get_color() == 1:
        root = self.rotate_right(root)

      # changes color to make sure red-black property is valid, case where both are red
      if root.get_left().get_color() == 1 and root.get_right().get_color() == 1:
        self.flip_colors(root)

      return root

    # will be used to traverse and look for a specific
    # username if the user want to play as that
    def search(self, data):
      return self.search_recursive(self.root, data)

    def search_recursive(self, current, data):
      if current == self.NIL:
        return False
      elif current.get_data() == data:
        return True
      elif data < current.get_data():
        return self.search_recursive(current.get_left(), data)
      else:
        return self.search_recursive(current.get_right(), data)

    def keep_playing(self, data):
      if self.root != self.NIL:
        self.keep_playing_recursive(self.root, data)

    def keep_playing_recursive(self, current, data):
      if current == self.NIL:
        print(f"Did not find match for: {data}")
        return
      
      elif data < current.get_data():
        self.keep_playing_recursive(current.get_left(), data)
      elif data > current.get_data():
        self.keep_playing_recursive(current.get_right(), data)
      else: # data == current.get_data()
        current.play_avatar()
      return

    def rotate_left(self, current_node):
      right_child = current_node.get_right()
      current_node.set_right(right_child.get_left())

      if right_child.get_left() != self.NIL:
        right_child.get_left().set_parent(current_node)

      right_child.set_parent(current_node.get_parent())

      if current_node.get_parent() is None:
        self.root = right_child
      elif current_node == current_node.get_parent().get_left():
        current_node.get_parent().set_left(right_child)
      else:
        current_node.get_parent().set_right(right_child)

      right_child.set_left(current_node)
      current_node.set_parent(right_child)

      right_child.set_color(current_node.get_color())
      current_node.set_color(1)  # set color to red

      return right_child

    def rotate_right(self, current_node):
      left_child = current_node.get_left()
      current_node.set_left(left_child.get_right())

      if left_child.get_right() != self.NIL:
        left_child.get_right().set_parent(current_node)

      left_child.set_parent(current_node.get_parent())

      if current_node.get_parent() is None:
        self.root = left_child
      elif current_node == current_node.get_parent().get_right():
        current_node.get_parent().set_right(left_child)
      else:
        current_node.get_parent().set_left(left_child)

      left_child.set_right(current_node)
      current_node.set_parent(left_child)

      left_child.set_color(current_node.get_color())
      current_node.set_color(1)  # sets color to red

      return left_child

    def flip_colors(self, current_node):
      # sets color to red
      current_node.set_color(1)
      # sets color to black
      current_node.get_left().set_color(0)
      current_node.get_right().set_color(0)

    def inorder(self):
      print("All your saved usernames:")
      self.inorder_recursive(self.root)
      print("\n")

    def inorder_recursive(self, node):
      if node != self.NIL:
        self.inorder_recursive(node.get_left())
        print(f"Avatar Name: {str(node.get_data())}")
        self.inorder_recursive(node.get_right())