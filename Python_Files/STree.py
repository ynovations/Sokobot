import datetime
from queue import Queue
import os
from Create_State import *

class STree:
    KEEPSEARCHING = True

    def __init__(self, root_mapData, root_itemsData):
        self.root = State(root_mapData, root_itemsData)  # Initialize the root state


    def get_root(self):
        return self.root

    @staticmethod
    def solution(solution, generated, repeated, fringe, seen, start):
        STree.KEEPSEARCHING = False
        time = (datetime.datetime.now() - start).total_seconds()
        return [
            solution.get_path(),
            "\n",
            "Generated: " + str(generated),
            "Repeated: " + str(repeated),
            "Fringe: " + str(fringe),
            "Explored: " + str(seen),
            "Duration: " + str(time)
        ]

    @staticmethod
    def failure():
        return ["Search Completed and No Solution Found"]

    def bfs(self):
        STree.KEEPSEARCHING = True
        start = datetime.datetime.now()
        rep = 0
        gen = 1
        node = self.root
        explored = set()
        frontier = Queue()
        frontier.put(node)

        if node.is_goal():
            return self.solution(node, gen, rep, frontier.qsize(), len(explored), start)

        while STree.KEEPSEARCHING:
            if frontier.empty():
                return self.failure()
            node = frontier.get()
            explored.add(node.get_state_string())

            for move in node.get_valid_moves():
                child = State(node.get_map_data(), node.get_items_data())  # Initialize child state with the same mapData and itemsData
                child.child_from_parent(node, move)
                gen += 1
                if child.get_state_string() not in explored and child not in frontier.queue:
                    if child.is_goal():
                        return self.solution(child, gen, rep, frontier.qsize(), len(explored), start)
                    frontier.put(child)
                elif child.get_state_string() in explored:
                    rep += 1
