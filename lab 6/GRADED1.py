import math

class Node:
    def __init__(self, state, parent=None, actions=[], totalCost=math.inf):
        self.state = state
        self.actions = actions
        self.parent = parent
        self.totalCost = totalCost

graph = {
    'Baltimore': Node('Baltimore', None, [('Atlanta', 14), ('Chicago', 15)], 0),
    'Chicago': Node('Chicago', None, [('Dallas', 18), ('Denver', 18), ('Baltimore', 15), ('Atlanta', 14)], 0),
    'Atlanta': Node('Atlanta', None, [('Baltimore', 14), ('Dallas', 15), ('Denver', 24), ('Chicago', 14)], 0),
    'Bakersfield': Node('Bakersfield', None, [('Denver', 19), ('Dallas', 25)], 0),
    'Denver': Node('Denver', None, [('Atlanta', 24), ('Chicago', 18), ('Bakersfield', 19)], 0),
    'Dallas': Node('Dallas', None, [('Atlanta', 15), ('Bakersfield', 25), ('Chicago', 18)], 0),
}

def findMin(frontier):
    minCost = math.inf
    minNode = None
    for node in frontier:
        if graph[node].totalCost < minCost:
            minCost = graph[node].totalCost
            minNode = node
    return minNode

def actionSequence(graph, initialstate, goalstate):
    solution = [goalstate]
    currentParent = graph[goalstate].parent
    while currentParent != initialstate:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.append(initialstate)
    solution.reverse()
    return solution

def UCS():
    initialstate = 'Baltimore'
    goalState = 'Dallas'
    frontier = [initialstate]
    explored = []
    graph[initialstate].totalCost = 0

    while frontier:
        currentNode = findMin(frontier)
        frontier.remove(currentNode)
        explored.append(currentNode)

        if currentNode == goalState:
            return actionSequence(graph, initialstate, goalState)

        for child in graph[currentNode].actions:
            child_state, cost = child
            if child_state not in explored:
                if child_state not in frontier:
                    graph[child_state].parent = currentNode
                    graph[child_state].totalCost = graph[currentNode].totalCost + cost
                    frontier.append(child_state)
                elif graph[child_state].totalCost > graph[currentNode].totalCost + cost:
                    graph[child_state].parent = currentNode
                    graph[child_state].totalCost = graph[currentNode].totalCost + cost

solution = UCS()
print(solution)
