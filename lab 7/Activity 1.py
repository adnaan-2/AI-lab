# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math


class Node:
    def __init__(self, state, parent, actions, totalCost, heuristic):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalCost = totalCost
        self.heuristic = heuristic


def findMin(frontier):
    minV = math.inf
    node = None
    for i in frontier:
        if minV > frontier[i][1]:
            minV = frontier[i][1]
            node = i
    return node


def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent is not None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution


def Astar():
    initialState = 'A'
    goalState = 'Y'

    graph = {
        'A': Node('A', None, [('F', 1)], 0, (0, 0)),
        'B': Node('B', None, [('G', 1), ('C', 1)], 0, (2, 0)),
        'C': Node('C', None, [('B', 1), ('D', 1)], 0, (3, 0)),
        'D': Node('D', None, [('C', 1), ('E', 1)], 0, (4, 0)),
        'E': Node('E', None, [('D', 1)], 0, (5, 0)),
        'F': Node('F', None, [('A', 1), ('H', 1)], 0, (0, 1)),
        'G': Node('G', None, [('B', 1), ('J', 1)], 0, (2, 1)),
        'H': Node('H', None, [('F', 1), ('I', 1), ('M', 1)], 0, (0, 2)),
        'I': Node('I', None, [('H', 1), ('J', 1), ('N', 1)], 0, (1, 2)),
        'J': Node('J', None, [('G', 1), ('I', 1)], 0, (2, 2)),
        'K': Node('K', None, [('L', 1), ('P', 1)], 0, (4, 2)),
        'L': Node('L', None, [('K', 1), ('Q', 1)], 0, (5, 2)),
        'M': Node('M', None, [('H', 1), ('N', 1), ('R', 1)], 0, (0, 3)),
        'N': Node('N', None, [('I', 1), ('M', 1), ('S', 1)], 0, (1, 3)),
        'O': Node('O', None, [('P', 1), ('U', 1)], 0, (3, 3)),
        'P': Node('P', None, [('O', 1), ('Q', 1)], 0, (4, 3)),
        'Q': Node('Q', None, [('L', 1), ('P', 1), ('V', 1)], 0, (5, 3)),
        'R': Node('R', None, [('N', 1), ('S', 1)], 0, (0, 4)),
        'S': Node('S', None, [('N', 1), ('R', 1), ('T', 1)], 0, (1, 4)),
        'T': Node('T', None, [('S', 1), ('U', 1), ('W', 1)], 0, (2, 4)),
        'U': Node('U', None, [('O', 1), ('T', 1)], 0, (3, 4)),
        'V': Node('V', None, [('Q', 1), ('Y', 1)], 0, (5, 4)),
        'W': Node('W', None, [('T', 1)], 0, (2, 5)),
        'X': Node('X', None, [('Y', 1)], 0, (4, 5)),
        'Y': Node('Y', None, [('V', 1), ('X', 1)], 0, (5, 5)),
    }

    frontier = {}
    heuristicCost = math.sqrt((graph[goalState].heuristic[0] - graph[initialState].heuristic[0]) ** 2 +
                              (graph[goalState].heuristic[1] - graph[initialState].heuristic[1]) ** 2)
    frontier[initialState] = (None, heuristicCost)
    explored = {}

    while len(frontier) != 0:
        currentNode = findMin(frontier)
        del frontier[currentNode]

        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)

        heuristicCost = math.sqrt((graph[goalState].heuristic[0] - graph[currentNode].heuristic[0]) ** 2 +
                                  (graph[goalState].heuristic[1] - graph[currentNode].heuristic[1]) ** 2)
        currentCost = graph[currentNode].totalCost
        explored[currentNode] = (graph[currentNode].parent, heuristicCost + currentCost)

        for child, cost in graph[currentNode].actions:
            currentCost = cost + graph[currentNode].totalCost
            heuristicCost = math.sqrt((graph[goalState].heuristic[0] - graph[child].heuristic[0]) ** 2 +
                                      (graph[goalState].heuristic[1] - graph[child].heuristic[1]) ** 2)
            if child in explored:
                if graph[child].parent == currentNode or child == initialState or \
                        explored[child][1] <= currentCost + heuristicCost:
                    continue

            if child not in frontier:
                graph[child].parent = currentNode
                graph[child].totalCost = currentCost
                frontier[child] = (graph[child].parent, currentCost + heuristicCost)
            else:
                if frontier[child][1] < currentCost + heuristicCost:
                    graph[child].parent = frontier[child][0]
                    graph[child].totalCost = frontier[child][1] - heuristicCost
                else:
                    frontier[child] = (currentNode, currentCost + heuristicCost)
                    graph[child].parent = frontier[child][0]
                    graph[child].totalCost = currentCost


solution = Astar()
print(solution)