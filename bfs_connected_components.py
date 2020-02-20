# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
            #print("value for node ",node,neighbours)

            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
            #print("result of queue: ",queue)
    # print(explored)
    return explored


# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B', 'E'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}
print(bfs_connected_component(graph, 'A'))
#bfs_connected_component(graph, 'A')  # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']