"""
File: test_avatar.py

Author: Josue Lopez

Course/Class and section: CS302-002

Date: 2nd December 2023

Program: CS302-002-program4/5

Description: Testing file for whole program. This file tests the methods
              from each file and makes sure they work as intended. For
              further information regarding any individual method
              please see the corresponding file, all method information
              will be detailed in there.
"""
from avatar import *
from node import *
from main import *
from game import *
from rbtree import *
import pytest


# testing avatar class
def test___init__avatar():
  obj = Avatar()
  obj2 = Avatar()
  assert obj.get_level() == 0 and obj2._level == 0

def test_increase_level():
  obj = Avatar()
  obj.increase_level()
  obj2 = Avatar()
  obj2.increase_level()
  assert obj.get_level() == 1 and obj2._level == 1

def test_get_level():
  obj = Avatar()
  assert obj.get_level() == 0 and obj._level == 0

# TESTING MARKSMAN CLASS BELOW

def test___init__marksman():
  obj = Marksman()
  obj2 = Marksman()
  assert obj.amount_of_people_deleted() == 0 and obj2._people_deleted == 0

def test_delete_person():
  obj = Marksman()
  obj.delete_person()
  obj2 = Marksman()
  obj2.delete_person()
  assert obj.amount_of_people_deleted() == 1 and obj2._people_deleted == 1

def test_amount_of_people_deleted():
  obj = Marksman()
  obj2 = Marksman()
  assert obj.amount_of_people_deleted() == 0 and obj2._people_deleted == 0

# TESTING ENGINEER CLASS BELOW
def test___init__engineer():
  obj = Engineer()
  assert obj.amount_of_items_fixed() == 0

def test_amount_of_items_fixed():
  obj = Engineer()
  obj2 = Engineer()
  assert obj.amount_of_items_fixed() == 0 and obj2._items_fixed == 0

def test_fix_item():
  obj = Engineer()
  obj.fix_item()
  obj2 = Engineer()
  obj2.fix_item()
  assert obj.amount_of_items_fixed() == 1 and obj2._items_fixed == 1

# TESTING MEDIC CLASS BELOW
def test___init__medic():
  obj = Medic()
  obj2 = Medic()
  assert obj.amount_of_people_healed() == 0 and obj2._people_healed == 0

def test_amount_of_people_healed():
  obj = Medic()
  obj2 = Medic()
  assert obj.amount_of_people_healed() == 0 and obj2._people_healed == 0 

def test_heal_person():
  obj = Medic()
  obj.heal_person()
  obj2 = Medic()
  obj2.heal_person()
  assert obj.amount_of_people_healed() == 1 and obj2._people_healed == 1

# TESTING NODE CLASS

def test__init__node():
  obj = Node()
  assert obj._data == None
  assert obj._color == 0
  assert obj._parent == None
  assert obj._left == None
  assert obj._right == None
  assert obj._player == None
  # still need to make game class which will have
  # player to pick from, not done yet

# testing getters
def test_get_data():
  obj = Node()
  obj2 = Node("PYTHON") # username
  assert obj.get_data() == None and obj._data == None
  assert obj2.get_data() == "PYTHON" and obj2._data == "PYTHON"

def test_get_parent():
  obj = Node()
  obj2 = Node()
  obj2._parent = "testing"
  assert obj.get_parent() == None and obj._parent == None
  assert obj2.get_parent() == "testing" and obj2._parent == "testing"

def test_get_color():
  obj = Node()
  obj2 = Node()
  obj2._color = 1
  assert obj.get_color() == 0 and obj._color == 0
  assert obj2.get_color() == 1 and obj2._color == 1

def test_get_left():
  obj = Node()
  obj2 = Node()
  obj2._left = obj
  assert obj.get_left() == None and obj._left == None
  assert obj2.get_left() != None and obj2._left != None

def test_get_right():
  obj = Node()
  obj2 = Node()
  obj2._right = obj
  assert obj.get_right() == None and obj._right == None
  assert obj2.get_right() != None and obj2._right != None

# setters for NODE CLASS

def test_set_data():
  obj = Node()
  obj2 = Node()
  obj2.set_data("PYTHON")
  assert obj.get_data() == None and obj._data == None
  assert obj2.get_data() == "PYTHON" and obj2._data == "PYTHON"

def test_set_color():
  obj = Node()
  obj2 = Node()
  obj2.set_color(1)
  assert obj.get_color() == 0 and obj._color == 0
  assert obj2.get_color() == 1 and obj2._color == 1

def test_set_parent():
  obj = Node()
  obj2 = Node()
  obj2.set_parent(obj)
  assert obj.get_parent() == None and obj._parent == None
  assert obj2.get_parent() != None  and obj2._parent != None

def test_set_left():
  obj = Node()
  obj2 = Node()
  obj2.set_left(obj)
  assert obj.get_left() == None and obj._left == None
  assert obj2.get_left() != None and obj2._left != None

def test_set_right():
  obj = Node()
  obj2 = Node()
  obj2.set_right(obj)
  assert obj.get_right() == None and obj._right == None
  assert obj2.get_right() != None and obj2._right != None

# TESTING GAME CLASS

def test__init__game():
  obj = Game()
  assert len(obj._items) == 0 and obj._items == []

def test_buy_item():
  obj = Game()
  obj.buy_item("item")
  assert len(obj._items) == 1

def test_show_items():
  obj = Game()
  assert obj.show_items() == None

def test_menu():
  obj = Game()
  assert obj.menu() == None

# TESTING MAIN FILE

def test_instructions():
  assert instructions() == None

def test_goodbye_message():
  assert goodbye_message() == None

# TESTING TREE CLASS

def test__init__tree():
  obj = Tree()
  assert type(obj.NIL) == type(Node())
  assert type(obj.root) == type(obj.NIL)

def test_insert():
  obj = Tree()
  assert obj.insert("PYTHON", 3) == True
  assert obj.insert("PYTHON", 2) == False

def test_insert_recursive():
  obj = Tree()
  temp_node = Node()
  temp = obj.insert_recursive(obj.root, temp_node)
  assert temp == temp_node

def test_search():
  obj = Tree()
  result = obj.search("Python")
  obj.insert("Python", 3)
  result_two = obj.search("Python")
  assert result == False and result_two == True

def test_search_recursive():
  obj = Tree()
  result = obj.search_recursive(obj.root,"Python")
  obj.insert("Python", 2)
  result_two = obj.search_recursive(obj.root, "Python")
  assert result == False and result_two == True

def test_keep_playing():
  obj = Tree()
  obj2 = Tree()
  obj2.insert("Python", 2)
  assert obj.keep_playing("Python") == None
  assert obj2.keep_playing("Python") == None

def test_keep_playing_recursive():
  obj = Tree()
  obj2 = Tree()
  assert obj.keep_playing_recursive(obj.root, "Python") == None

