# Dijkstra's Algorithm

import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0, start)]  # (distance, node)

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist


# Main
print("---- Dijkstra Algorithm ----")
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # remove if directed

start = int(input("Enter source vertex: "))

distances = dijkstra(graph, start)

print("Shortest distances from source:")
for i in range(n):
    print(f"To {i}:", distances[i])