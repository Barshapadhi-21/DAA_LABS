# Kruskal's Algorithm

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight
    parent = list(range(n))
    rank = [0] * n

    total_cost = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            total_cost += w

    return total_cost


# Main
print("---- Kruskal's Algorithm ----")
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

cost = kruskal(n, edges)

print("Minimum Spanning Tree cost:", cost)