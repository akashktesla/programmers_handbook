from collections import deque


def bfs(node,graph,visited,q):
    q.append(node)
    prev = [None]* len(graph)
    while len(q)!=0:
        node = q.popleft()
        neighbours = graph[node]
        for next in neighbours:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                prev[next] = node
    
    return prev



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
    q = deque()
    prev = bfs(node,graph,visited,q)
    print(f"Prev: {prev}")

