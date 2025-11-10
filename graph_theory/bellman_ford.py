def bellman_ford(graph,N,S):
    V = len(graph)
    dist = [float('inf')]*N
    dist[S] = 0
    for i in range(V-1):
        for edge in graph:
            newCost = dist[edge[0]] + edge[2]
            # print(f"newCost: {newCost}")
            if newCost < dist[edge[1]]:
                dist[edge[1]] = newCost
    for i in range(V-1):
        for edge in graph:
            newCost = dist[edge[0]] + edge[2]
            if newCost < dist[edge[1]]:
                dist[edge[1]] = float('-inf')
    return dist


if __name__ == "__main__":
    graph = [
        (0, 1, 1),
        (1, 2, 3),
        (2, 3, 2),
        (3, 1, -6),  
        (0, 4, 10),
    ]
    N = 5
    S = 0
    dist = bellman_ford(graph, N, S)
    print(f"dist: {dist}")

