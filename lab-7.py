# Weighted Interval Scheduling using Dynamic Programming

def binary_search(jobs, i):
    """Find the last non-conflicting job before job i"""
    low = 0
    high = i - 1

    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][1] <= jobs[i][0]:
            if jobs[mid + 1][1] <= jobs[i][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1


def weighted_interval_scheduling(jobs):
    # Sort jobs by finish time
    jobs.sort(key=lambda x: x[1])

    n = len(jobs)
    dp = [0] * n

    # First job profit
    dp[0] = jobs[0][2]

    for i in range(1, n):
        # Include current job
        incl_profit = jobs[i][2]
        l = binary_search(jobs, i)
        if l != -1:
            incl_profit += dp[l]

        # Exclude current job
        dp[i] = max(incl_profit, dp[i - 1])

    return dp[n - 1]


# Main Program
print("---- Weighted Interval Scheduling ----")

n = int(input("Enter number of jobs: "))
jobs = []

print("Enter jobs as: start finish profit")
for _ in range(n):
    s, f, p = map(int, input().split())
    jobs.append((s, f, p))

max_profit = weighted_interval_scheduling(jobs)

print("Maximum profit:", max_profit)