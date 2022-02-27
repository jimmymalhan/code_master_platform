# You are given a 0-indexed 2D integer array tires where tires[i] = [fi, ri] indicates that the ith tire can finish its xth successive lap in fi * ri(x-1) seconds.

# For example, if fi = 3 and ri = 2, then the tire would finish its 1st lap in 3 seconds, its 2nd lap in 3 * 2 = 6 seconds, its 3rd lap in 3 * 22 = 12 seconds, etc.
# You are also given an integer changeTime and an integer numLaps.

# The race consists of numLaps laps and you may start the race with any tire. You have an unlimited supply of each tire and after every lap, you may change to any given tire (including the current tire type) if you wait changeTime seconds.

# Return the minimum time to finish the race.

# Input: tires = [[2,3],[3,4]], changeTime = 5, numLaps = 4
# Output: 21
# Explanation: 
# Lap 1: Start with tire 0 and finish the lap in 2 seconds.
# Lap 2: Continue with tire 0 and finish the lap in 2 * 3 = 6 seconds.
# Lap 3: Change tires to a new tire 0 for 5 seconds and then finish the lap in another 2 seconds.
# Lap 4: Continue with tire 0 and finish the lap in 2 * 3 = 6 seconds.
# Total time = 2 + 6 + 5 + 2 + 6 = 21 seconds.
# The minimum time to complete the race is 21 seconds.

from typing import List

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        minimum = [] # minimum[i] represents for the min time to complete i laps without changing a  tire
        total = [0] * len(tires)
        # the worst case is: fi = 1, ri = 2, changeTime = 10 ** 5
        # this while loop will be computed for at most math.ceil(math.log2(10 ** 5 + 1)) = 17 times
        while True:
            for t in range(len(tires)):
                total[t] += tires[t][0]
                tires[t][0] *= tires[t][1]
            minimum.append(min(total))
            # if the minimum cost is greater than changing a new tire, we stop looping
            if minimum[-1] > changeTime + minimum[0]: break

        # dp
        dp = [float('inf')] * numLaps
        for l in range(numLaps):
            for pre in range(len(minimum)):
                if l - pre - 1 < 0:
                    dp[l] = min(dp[l], minimum[pre])
                    break
                dp[l] = min(dp[l], minimum[pre] + dp[l - pre - 1] + changeTime)
        return dp[-1]

print(Solution().minimumFinishTime([[2,3],[3,4]], 5, 4))