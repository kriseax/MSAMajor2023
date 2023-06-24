import math
def dijkstra(graph, start):
    tentative, confirmed = {}, {}

    #add start node to confirmed
    confirmed[start] = (0, "-")

    #place start node's neighbors on the tentative list
    for node, distance in graph[start].items():
        tentative[node] = distance

    #set next to the node just added
    next = start

    while tentative:
        shortest_distance = math.inf

        #select node from tentative list with lowest cost
        for node, distance in tentative.items():

            #determine lowest cost node
            if distance < shortest_distance:
                shortest_distance = distance
                next = node
        
        #add lowest cost node to confirmed and update next, remove next node from tentative
        confirmed[next] = (shortest_distance, next)
        tentative.pop(next)

        #place next nodes neighbors on tentative list
        #if neighbor not in tentative, add to tentative. If neighbor in tentative update if necessary 
        for node, distance in graph[next].items():
            cost = confirmed[next][0] + distance

            if (node in confirmed):
                continue
            elif (node in tentative) and cost < tentative[node]:
                tentative[node] = cost
            elif node not in tentative:
                tentative[node] = cost
    return confirmed

def main():
    graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
    }

    start_node = 'A'

    distances = dijkstra(graph, start_node)

    print("Shortest distances from node", start_node)
    for node, distance in distances.items():
        print(node, "->", distance)

main()
