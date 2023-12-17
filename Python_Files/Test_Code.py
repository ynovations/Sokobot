#This file tests the Create_State file by initiating a State and its children, and then printing out the results

from Test_Map import *
from Create_State import *


# Initiate State
Node0 = State(sample_map, sample_items)

print("Node0 (Initial State):")
Node0.print_state()
valid_moves = Node0.get_valid_moves()
print("Valid Moves:", valid_moves)

# Test child_from_parent for Node1
Node1 = State(Node0.mapData, Node0.itemsData)
Node1.child_from_parent(Node0, valid_moves[0])

# Print Node1 after moving
print("Node1 (New State):")
Node1.print_state()
valid_moves = Node1.get_valid_moves()
print("Valid Moves:", valid_moves)

# Create Node2 from Node1
Node2 = State(Node1.mapData, Node1.itemsData)
Node2.child_from_parent(Node1, valid_moves[0])

# Print Node2
print("Node2 (Third State):")
Node2.print_state()
valid_moves = Node2.get_valid_moves()
print("Valid Moves:", valid_moves)

