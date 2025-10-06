# Depth First Search 

def dfs(node,graph,visited):
    print(visited)
    if visited[node]:
        return 
    visited[node] = True
    neighbours = graph[node]
    for next in neighbours:
        dfs(next,graph,visited)


if __name__ == "__main__":
    graph = {
            0: [1, 2],
            1: [3, 4],
            2: [5, 6],
            3: [7],
            4: [0, 5],
            5: [8],
            6: [5, 9],
            7: [],
            8: [],
            9: [2]
            }

    visited = [False]* len(graph)
    node = 1
    dfs(node,graph,visited)
