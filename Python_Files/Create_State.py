#This file contains all the logic to create the State (Parent-Child Relationship) based on Valid Moves and the given MapData and ItemsData. 
#We will use the State to populate our Search Tree. 


class State:

    #Initializes the State and it's Children (and Parent) State.

    def __init__(self, mapData, itemsData, par=None, dir=None):
        if par is None and dir is None:
            # Initialization for the initial state
            #2D Deep Copy
            self.mapData = [row[:] for row in mapData]
            self.itemsData = [row[:] for row in itemsData]
            self.parent = None
            self.cost = 0
            self.path = ""
            self.statestring = ""
            self.x = None 
            self.y = None
            self.find_player_position()


            for row in itemsData:
                for c in row:
                    self.statestring += c
        
        else:
            self.child_from_parent(par, dir)

    def child_from_parent(self, par, dir):
        # Initialization for subsequent states
        self.parent = par
        self.cost = par.cost + 1
        self.path = par.path + dir

        # Make the move
        tmp_items_data = self.move_player(par, dir)
        self.itemsData = [row[:] for row in tmp_items_data]

        if dir == 'u':
            self.x = par.x - 1
            self.y = par.y
        elif dir == 'd':
            self.x = par.x + 1
            self.y = par.y
        elif dir == 'l':
            self.x = par.x
            self.y = par.y - 1
        elif dir == 'r':
            self.x = par.x
            self.y = par.y + 1

        # 2D deep copy
        self.mapData = [row[:] for row in par.mapData]

        # Recompute the statestring
        self.statestring = ""
        for row in self.itemsData:
            for c in row:
                self.statestring += c

    #This Method moves the Player (@) and returns an updated ItemsData. 
    #The updated ItemsData will be the nodes in our search tree. 
    # ItemsData contain info on the position of all boxes and the Player, in any given State.

    def move_player(self, par, dir):
        # Deep copy of the map and items
        new_mapData = [row[:] for row in par.mapData]
        new_itemsData = [row[:] for row in par.itemsData]

        x, y = self.x, self.y

        if dir == 'u':
            if new_itemsData[x - 1][y] == '$':
                self.cost += 1
                if new_mapData[x - 2][y] in [' ', '.']:
                    new_itemsData[x - 2][y] = '$'
                    new_itemsData[x - 1][y] = '@'
                    new_itemsData[x][y] = ' '

            if new_mapData[x - 1][y] in [' ', '.']:
                new_itemsData[x - 1][y] = '@'
                new_itemsData[x][y] = ' '

        if dir == 'd':
            if new_itemsData[x + 1][y] == '$':
                self.cost += 1
                if new_mapData[x + 2][y] in [' ', '.']:
                    new_itemsData[x + 2][y] = '$'
                    new_itemsData[x + 1][y] = '@'
                    new_itemsData[x][y] = ' '

            if new_mapData[x + 1][y] in [' ', '.']:
                new_itemsData[x + 1][y] = '@'
                new_itemsData[x][y] = ' '

        elif dir == 'l':
            if new_itemsData[x][y - 1] == '$':
                self.cost += 1
                if new_mapData[x][y - 2] in [' ', '.']:
                    new_itemsData[x][y - 2] = '$'
                    new_itemsData[x][y - 1] = '@'
                    new_itemsData[x][y] = ' '

            if new_mapData[x][y - 1] in [' ', '.']:
                new_itemsData[x][y - 1] = '@'
                new_itemsData[x][y] = ' '

        elif dir == 'r':
            if new_itemsData[x][y + 1] == '$':
                self.cost += 1
                if new_mapData[x][y + 2] in [' ', '.']:
                    new_itemsData[x][y + 2] = '$'
                    new_itemsData[x][y + 1] = '@'
                    new_itemsData[x][y] = ' '

            if new_mapData[x][y + 1] in [' ', '.']:
                new_itemsData[x][y + 1] = '@'
                new_itemsData[x][y] = ' '

        return new_itemsData


    def find_player_position(self):
        for i in range(len(self.mapData)):
            for j in range(len(self.mapData[i])):
                if self.itemsData[i][j] == '@':
                    self.x = i  # Store the player's x position
                    self.y = j  # Store the player's y position
                    return self.x, self.y

    #These code below checks the Valid Moves and they return an Array of Valid Moves given a MapData and ItemsData.
    #An element in the array of valid moves can be fed to the function: "child_from_parent" so a new Child State (node) will be created.

    def is_up_valid(self):
        up_map = self.mapData[self.x - 1][self.y]
        up_items = self.itemsData[self.x - 1][self.y]

        # If you're below a wall
        if up_map == '#':
            print('There is a wall')
            return False

        # Check if there's an overflow in the map
        if len(self.mapData[self.x - 2]) <= self.y:
            print("Overflow")
            return False

        # Check if the space two rows up can accept a box (i.e., it's an empty space or goal)
        up_map2 = self.mapData[self.x - 2][self.y]
        up_items2 = self.itemsData[self.x - 2][self.y]

        if (up_items == '$') and (up_items2 == '$' or up_map2 == '#'):
            print("Box is Blocked")
            return False

        if (up_items == '$') and (up_map2 == ' ' or up_map2 == '.'):
            print("We can move the Box")
            return True

        # If you can move up, set the up variable and check open space
        if up_map in (' ', '.'):
            print('Open Space or Goal')
            return True

        # Default to False
        return False

    def is_down_valid(self):
        down_map = self.mapData[self.x + 1][self.y]
        down_items = self.itemsData[self.x + 1][self.y]

        # If you're above a wall
        if down_map == '#':
            print('There is a wall')
            return False

        # Check for overflow
        if len(self.mapData[self.x + 2]) <= self.y:
            print("Overflow")
            return False

        # Check if the space two rows down can accept a box (i.e., it's an empty space or goal)
        down_map2 = self.mapData[self.x + 2][self.y]
        down_items2 = self.itemsData[self.x + 2][self.y]

        if (down_items == '$') and (down_items2 == '$' or down_map2 == '#'):
            print("Box is Blocked")
            return False

        if (down_items == '$') and (down_map2 == ' ' or down_map2 == '.'):
            print("We can move the Box")
            return True

        if down_map in (' ', '.'):
            print('Open Space or Goal')
            return True

        # Default to False for unforeseen cases
        return False

    def is_left_valid(self):
        left_map = self.mapData[self.x][self.y - 1]
        left_items = self.itemsData[self.x][self.y - 1]

        # If you're right of a wall
        if left_map == '#':
            print('There is a wall')
            return False

        if self.y <= 1:
            print("Overflow")
            return False

        left_map2 = self.mapData[self.x][self.y - 2]
        left_items2 = self.itemsData[self.x][self.y - 2]

        # Check if the space two columns left can accept a box (i.e., it's an empty space or goal)
        if (left_items == '$') and (left_items2 == '$' or left_map2 == '#'):
            print("Box is Blocked")
            return False
        if (left_items == '$') and (left_map2 == ' ' or left_map2 == '.'):
            print("We can move the Box")
            return True

        if left_map in (' ', '.'):
            print('Open Space or Goal')
            return True

        # Default to False for unforeseen cases
        return False

    def is_right_valid(self):
        right_map = self.mapData[self.x][self.y + 1]
        right_items = self.itemsData[self.x][self.y + 1]

        # If you're left of a wall
        if right_map == '#':
            print('There is a wall')
            return False

        if len(self.mapData[self.x]) <= self.y + 2:
            print("Overflow")
            return False

        right_map2 = self.mapData[self.x][self.y + 2]
        right_items2 = self.itemsData[self.x][self.y + 2]

        # Check if the space two columns right can accept a box (i.e., it's an empty space or goal)
        if (right_items == '$' or right_items == '*') and (right_items2 == '$' or right_map2 == '#'):
            print("Box is Blocked")
            return False
        if (right_items == '$' or right_items == '*') and (right_map2 in (' ', '.')):
            print("We can move the Box")
            return True

        if right_map in (' ', '.'):
            print('Open Space or Goal')
            return True

        # Default to False for unforeseen cases
        return False

    def get_valid_moves(self):
        moves = []

        if self.is_up_valid():
            moves.append('u')

        if self.is_down_valid():
            moves.append('d')

        if self.is_left_valid():
            moves.append('l')

        if self.is_right_valid():
            moves.append('r')

        return moves


    #Other helper functions used in STree:
    
    def get_path(self):
        return self.path
    
    def is_goal(self):
        for i in range(len(self.mapData)):
            for j in range(len(self.mapData[i])):
                if self.itemsData[i][j] == '$':
                    if self.mapData[i][j] != '.':
                        return False  # A '$' is not in the same position as '.'
        return True  # All '$' are in the same position as '.'

    def get_state_string(self):
        return self.statestring

    def get_map_data(self):
        return self.mapData
    
    def get_items_data(self):
        return self.itemsData

    #This method is just used for testing purposes, just to check if all the important States and Moves are being recorded properly.
    def print_state(self):
        print("This is Map")
        print(self.mapData)
        print("This is Items")
        print(self.itemsData)
        print("This is X and Y:", self.x, self.y)
        print("This is parent")
        if self.parent:
            for row in self.parent.itemsData:
                print("".join(row))
        else:
            print("No parent (Initial State)")