def dfs(node,graph,visited):
    visited_nodes = []
    if visited[node]:
        return []
    visited[node] = True
    neighbours = graph[node]
    for (next,_) in neighbours:
        v = dfs(next,graph,visited)
        visited_nodes.extend(v)
    visited_nodes.append(node)
    return visited_nodes


def top_sort(graph):
    n = len(graph)
    visited = [False]*n
    post_order = []
    for i in range(n):
        if not visited[i]:
            visited_nodes = dfs(i,graph,visited)
            post_order.extend(visited_nodes)
            # print(f"post_order: {post_order}")
    post_order.reverse()
    return post_order

def sssp_on_dag(source,graph):
    n = len(graph)
    order = top_sort(graph)
    dist = [float("inf")]*n
    dist[source] = 0
    for u in order:
        for (v,weight) in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    return dist



if __name__ == "__main__":
    # graph[u] = list of (v, weight)
    graph = {
            0: [(1, 2), (2, 4)],
            1: [(2, 1), (3, 7)],
            2: [(4, 3)],
            3: [(5, 1)],
            4: [(3, 2), (5, 5)],
            5: []
            }
    source = 0
    dist = sssp_on_dag(source, graph)
    print(f"dist: {dist}")

