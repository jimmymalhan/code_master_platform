# Problem Name: Longest Peak

# Problem Description:
# Write a function that takes in an array of integers and returns the length of the longest peak in the array.

# A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip(the highest value in the peak), at which point they become strictly decreasing. Atleast three integers are required to form a peak.

# For example, the integers `1, 4, 10, 2` form a peak, but the integers `4, 0, 10` don't and neither do the integers `1, 2, 2, 0``. Similarly, the integers `1, 2, 3`  don't form a peak because there aren't any strictly decreasing integers after the 3.

####################################
# Sample Input:
# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

# Sample Output:
# 6 # Because 0, 10, 6, 5, -1, -3 is the longest peak.

####################################
"""
Explain the solution:
- You can solve this question by interating through the array from left to right once.

- Iterate through the array from left to right, and treay every integer as the potential tip of a peak. To be the tip of a peak, an integer has to be strictly greater than its adjacent integers. What can you do when you find an actual tip?

- As you iterate through the array from left to right, whenever you find a tip of a peak, expand outwards from the tip until you no longer have a peak. Given what peaks look like and how many peaks can therefore fit in an array, realize that this process results in a linear-time algorithm. Make sure to keep track of the longest peak you find as you iterate through the array.

- O(n) time and O(1) space - where n is the length of the array.

##################
Detailed explanation of the Solution:
1. We start a loop where we start at index 1. This is because we need to check the peak first.
2. We check if the current index is a peak. 
3. If the index is not a peak, we move to the next index.
4. If the index is a peak, we check if the left and right index are greater than the current index.
5. If the left and right index are greater than the current index, we check if the left index is greater than the left index of the current index. 
6. If the left index is greater than the left index of the current index, we check if the right index is greater than the right index of the current index.
7. If the right index is greater than the right index of the current index, we check if the current peak length is greater than the current peak length.
8. If the current peak length is greater than the current peak length, we set the current peak length to the current peak length.
9. We then move to the right index of the current index.
10. We then loop back to 1 and check if the index is a peak.
11. We continue this loop until we reach the end of the array.
12. We return the current peak length.

"""
####################################

def longestPeak(array):
# 1. We start a loop where we start at index 1. This is because we need to check the peak first.
# 2. We check if the current index is a peak. 
# 3. If the index is not a peak, we move to the next index.
    longestPeakLength= 0
    i= 1
    while i<len(array) - 1:
        isPeak = array[i- 1] < array[i]and array[i] > array[i+1] # 2. We check if the current index is a peak. 

        if not isPeak:
            i += 1
            continue

# 4. If the index is a peak, we check if the left and right index are greater than the current index.
# 5. If the left and right index are greater than the current index, we check if the left index is greater than the left index of the current index. 
# 6. If the left index is greater than the left index of the current index, we check if the right index is greater than the right index of the current index.
# 7. If the right index is greater than the right index of the current index, we check if the current peak length is greater than the current peak length.

        leftIdx = i - 2 
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array)and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1
# 8. If the current peak length is greater than the current peak length, we set the current peak length to the current peak length.
# 9. We then move to the right index of the current index.
# 10. We then loop back to 1 and check if the index is a peak.
# 11. We continue this loop until we reach the end of the array.
# 12. We return the current peak length.
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength,currentPeakLength)
        i = rightIdx
    return longestPeakLength

print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3])) # 6 # Because 0, 10, 6, 5, -1, -3 is the longest peak.