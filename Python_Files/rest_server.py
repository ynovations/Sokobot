import urllib.parse
import re

from flask import Flask, request

from STree import STree



app = Flask(__name__)


@app.route('/solver', methods=['POST'])
def solver():
    data = request.form
    width = int(data['width'])  # Convert width to an integer
    height = int(data['height'])  # Convert height to an integer


    #Converts MapData String to a python Array
    mapData = urllib.parse.unquote_plus(data['mapData'], 'UTF-8')
    print('mapData')
    print(type(mapData))
    print(mapData)
    # Remove spaces between a comma and '#' or '.'
    mapData = mapData.replace('\n', '')
    mapData = re.sub(r",\s*'#'", ',#', mapData)
    mapData = re.sub(r",\s*#", ',#', mapData)
    mapData = re.sub(r",\s*'\.'", ',.', mapData)
    mapData = re.sub(r",\s*\.", ',.', mapData)
    mapData = re.sub(r",\s*' '", ', ', mapData)
    mapData = re.sub(r"\s\s,", ' ,', mapData)
    mapData = re.sub(r',\s*\[|\[\s*\[', ',[', mapData)
    mapData = re.sub(r'\]\s*\]', ']', mapData)
    mapData = re.sub(r'\s\s\]', ' ]', mapData)
    print(mapData)

    # Initialize variables to keep track of the current row and current character list
    current_row_map = []
    character_lists_map = []

    for char in mapData:
        if char in (' ', '#', '.'):
            current_row_map.append(char)
            if len(current_row_map) == width:
                character_lists_map.append(current_row_map)
                current_row_map = []
                if len(character_lists_map) == height:
                    break

    map_grid = character_lists_map

    print('map_grid')
    print(map_grid)
    #Converts MapData String to a python Array

    #Converts ItemsData String to a python Array
    itemsData = urllib.parse.unquote_plus(data['itemsData'], 'UTF-8')
    print('itemsData')
    print(type(itemsData))
    print(itemsData)
    # Remove spaces between a comma and '@' or '$'
    itemsData = itemsData.replace('\n', '')
    itemsData = re.sub(r",\s*'@'", ',@', itemsData)
    itemsData = re.sub(r",\s*@", ',@', itemsData)
    itemsData = re.sub(r",\s*'\$'", ',$', itemsData)
    itemsData = re.sub(r",\s*\$", ',$', itemsData)
    itemsData = re.sub(r",\s*' '", ', ', itemsData)
    itemsData = re.sub(r"\s\s,", ' ,', itemsData)
    itemsData = re.sub(r',\s*\[|\[\s*\[', ',[', itemsData)
    itemsData = re.sub(r'\]\s*\]', ']', itemsData)
    itemsData = re.sub(r'\s\s\]', ' ]', itemsData)
    print(itemsData)

    # Initialize variables to keep track of the current row and current character list
    current_row_item = []
    character_lists_item = []

    for char in itemsData:
        if char in ('@', '$', ' '):
            current_row_item.append(char)
            if len(current_row_item) == width:  # Assuming you want the same width as the map
                character_lists_item.append(current_row_item)
                current_row_item = []

    item_grid = character_lists_item

    print('item_grid')
    print(item_grid)

    #Converts ItemsData String to a python Array


    tree = STree(map_grid, item_grid)
    print("Root State:")
    root_state = tree.get_root()
    root_state.print_state()

    # Perform BFS to find a solution
    solution = tree.bfs()
    # Print the solution or failure message
    if solution:
        solution_string = str(solution[0])
        print(solution_string)
        return solution_string
    else:
        return {'message': 'No solution found.'}


app.run()
