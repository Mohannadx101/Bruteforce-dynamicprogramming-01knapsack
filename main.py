import time
import random

# 1. Brute Force Approach Recursive
def knapsack_brute_force(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weights[n - 1] > capacity:
        return knapsack_brute_force(weights, values, capacity, n - 1)
    else:
        include = values[n - 1] + knapsack_brute_force(weights, values, capacity - weights[n - 1], n - 1)
        exclude = knapsack_brute_force(weights, values, capacity, n - 1)
        return max(include, exclude)


# 2. Dynamic Programming Approach
def knapsack_dp(weights, values, capacity, n):
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtracking to find the selected items
    res = dp[n][capacity]
    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if res != dp[i - 1][w]:
            selected_items.append(i)  # storing item index
            res -= values[i - 1]
            w -= weights[i - 1]
    selected_items.reverse()
    return dp[n][capacity], selected_items


# Execution
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
n = len(values)

print(f"Standard Test Case: \nWeights {weights}, \nValues {values}, \nCap {capacity}\n")
print("-" * 30)

# Run Brute Force
start_time_bf = time.time()
bf_result = knapsack_brute_force(weights, values, capacity, n)
end_time_bf = time.time()
bf_time = (end_time_bf - start_time_bf) * 1000 #conversion to ms

print(f"Brute Force Result: {bf_result}")
print(f"Brute Force Time:   {bf_time:.4f} ms")
print("-" * 30)

# Run Dynamic Programming
start_time_dp = time.time()
dp_result = knapsack_dp(weights, values, capacity, n)
end_time_dp = time.time()
dp_time = (end_time_dp - start_time_dp) * 1000

print(f"DP Result:          {dp_result}")
print(f"DP Time:            {dp_time:.4f} ms")
print("-" * 30)
