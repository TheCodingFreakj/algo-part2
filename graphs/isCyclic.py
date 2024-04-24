

from collections import deque


def isCyclic(graph):
    visited = set()

    #iteration through all the keys
    for node in graph:
        if node not in visited:
            if bfs(graph, node, visited):
                return True
    return False


def bfs(graph, startingNode, visited):
    #as a part of bfs initializing the queue with the startnode and its parent
    #add the starting node to visited
    queue = deque([(startingNode, None)])
    visited.add(startingNode)
    
    while queue:
        #poping the top element from the queue
        node, parent = queue.popleft()
        
        #find the neighbours of the node poped out
        for neighbor in graph[node]:
            #checking if the neighbour is not visited
            if neighbor not in visited:
                #add the neighbournode and the parent node
                queue.append((neighbor, node))
                #mark it visited
                visited.add(neighbor)
            #if the neighbour is visted and it is not a parent then its cyclic    
            elif neighbor != parent:  
                return True
    return False


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}
print(isCyclic(graph))
