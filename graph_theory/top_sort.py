
def dfs(node,graph,visited):
    visited_nodes = []
    if visited[node]:
        return []
    visited[node] = True
    neighbours = graph[node]
    for next in neighbours:
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




if __name__ == "__main__":
    graph = {
            0: [1, 2],
            1: [3],
            2: [3, 4],
            3: [5],
            4: [5],
            5: [],
            }

    print(top_sort(graph))
