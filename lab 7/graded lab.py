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
    node = ''
    for i in frontier:
        if minV > frontier[i][1]:
            minV = frontier[i][1]
            node = i
    return node

def actionSequence(graph, initialState, goalState):
    solution = [goalState]
    currentParent = graph[goalState].parent
    while currentParent != None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

def aStar(graph, start, end):
    openList = set([start])
    closedList = set([])
    g = {} # Actual movement cost to each position from the start position
    parents = {} # Parents of nodes
    g[start] = 0
    parents[start] = start
    
    while len(openList) > 0:
        n = None
        for v in openList:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        
        if n == end or graph[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                if m not in openList and m not in closedList:
                    openList.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        
                        if m in closedList:
                            closedList.remove(m)
                            openList.add(m)
        
        if n == None:
            print('Path does not exist!')
            return None
        
        if n == end:
            path = []
            
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            
            path.append(start)
            path.reverse()
            
            print('Path found: {}'.format(path))
            return path
        
        openList.remove(n)
        closedList.add(n)
    
    print('Path does not exist!')
    return None

def get_neighbors(v):
    if v in graph:
        return graph[v]
    else:
        return None

# Example usage:
graph = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

def heuristic(n):
    H_dist = {
        'A': 1,
        'B': 1,
        'C': 1,
        'D': 1
    }
    
    return H_dist[n]

aStar(graph, 'A', 'D')
