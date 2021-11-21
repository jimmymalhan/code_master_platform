# You want to water n plants in your garden with a watering can. The plants are arranged in a row and are labeled from 0 to n - 1 from left to right where the ith plant is located at x = i. There is a river at x = -1 that you can refill your watering can at.

# Each plant needs a specific amount of water. You will water the plants in the following way:

# Water the plants in order from left to right.
# After watering the current plant, if you do not have enough water to completely water the next plant, return to the river to fully refill the watering can.
# You cannot refill the watering can early.
# You are initially at the river (i.e., x = -1). It takes one step to move one unit on the x-axis.

# Given a 0-indexed integer array plants of n integers, where plants[i] is the amount of water the ith plant needs, and an integer capacity representing the watering can capacity, return the number of steps needed to water all the plants.

# Input: plants = [2,2,3,3], capacity = 5
# Output: 14
# Explanation: Start at the river with a full watering can:
# - Walk to plant 0 (1 step) and water it. Watering can has 3 units of water.
# - Walk to plant 1 (1 step) and water it. Watering can has 1 unit of water.
# - Since you cannot completely water plant 2, walk back to the river to refill (2 steps).
# - Walk to plant 2 (3 steps) and water it. Watering can has 2 units of water.
# - Since you cannot completely water plant 3, walk back to the river to refill (3 steps).
# - Walk to plant 3 (4 steps) and water it.
# Steps needed = 1 + 1 + 2 + 3 + 3 + 4 = 14.

# concept:
# 1. if the current plant is not full, then we can water it
# 2. if the current plant is full, then we need to refill the watering can
from typing import List
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps, run_sum = 0, 0 # steps: total steps, run_sum: sum of water in watering can
        for i, p in enumerate(plants[:-1]): # i: index of current plant, p: current plant
            run_sum += p # add water to watering can
            if run_sum+plants[i+1] > capacity: # if the next plant is not full
                steps += 2*(i+1) # water the current plant twice
                run_sum = 0 # reset the watering can
        steps += len(plants) # add the last plant
        return steps

def main():
    plants = [2,2,3,3]
    capacity = 5

    solution = Solution()

    print(solution.wateringPlants(plants, capacity))

main()