#run this code to test if STree and Create_State is working properly.

from Create_State import State
from Test_Map import sample_map, sample_items
from STree import STree

# Initiate STree with the root State
tree = STree(sample_map, sample_items)

print("Root State:")
root_state = tree.get_root()
root_state.print_state()

# Perform BFS to find a solution
solution = tree.bfs()

# Print the solution or failure message
if solution:
    for line in solution:
        print(line)
else:
    print("No solution found.")
