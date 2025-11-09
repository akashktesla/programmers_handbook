from queue import PriorityQueue


def dijkstra(graph,graph_id_map,start):
    N = len(graph)
    print(f"N: {N}")
    visited = [False]*N
    dist = [float('inf')]*N
    dist[graph_id_map[start]] = 0
    pq = PriorityQueue()
    pq.put((0,start))
    while pq.qsize() != 0:
        minValue,index = pq.get()
        print(f"index: {index}")
        #mark as visited
        visited[graph_id_map[index]] = True
        neighbours = graph[index]
        for neighbour in neighbours:
            if visited[graph_id_map[neighbour[0]]]:
                continue
            newDist = dist[graph_id_map[index]] + neighbour[1]
            print(f"newDist: {newDist}")
            if newDist < dist[graph_id_map[neighbour[0]]]:
                pq.put((newDist,neighbour[0]))
                dist[graph_id_map[neighbour[0]]] = newDist
    return dist




if __name__ == "__main__":
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 5), ('D', 10)],
        'C': [('D', 3)],
        'D': []
    }
    graph_id_map = {
            "A":0,
            "B":1,
            "C":2,
            "D":3,
            }

    start = 'A';
    dist = dijkstra(graph, graph_id_map, start)
    print(f"Dist: {dist}")
