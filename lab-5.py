# Travelling Salesman Problem (TSP)
# Using Dynamic Programming (Held-Karp Algorithm)

import sys

def tsp_dp(dist):
    n = len(dist)
    VISITED_ALL = (1 << n) - 1

    # dp[mask][pos] = minimum cost to visit all cities in 'mask'
    # ending at 'pos'
    dp = [[-1] * n for _ in range(1 << n)]

    def visit(mask, pos):
        # If all cities are visited, return cost to go back to start
        if mask == VISITED_ALL:
            return dist[pos][0]

        # If already computed
        if dp[mask][pos] != -1:
            return dp[mask][pos]

        ans = sys.maxsize

        # Try visiting all unvisited cities
        for city in range(n):
            if (mask & (1 << city)) == 0:
                new_cost = dist[pos][city] + visit(mask | (1 << city), city)
                ans = min(ans, new_cost)

        dp[mask][pos] = ans
        return ans

    # Start from city 0 with only city 0 visited
    return visit(1, 0)


# Main Program
print("---- Travelling Salesman Problem (TSP) ----")
n = int(input("Enter number of cities: "))

print("Enter distance matrix:")
dist = []
for i in range(n):
    row = list(map(int, input().split()))
    dist.append(row)

# Calculate minimum cost
min_cost = tsp_dp(dist)

print("Minimum travelling cost:", min_cost)