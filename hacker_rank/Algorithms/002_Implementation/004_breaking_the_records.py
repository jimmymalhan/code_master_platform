# #                                  Count
# Game  Score  Minimum  Maximum   Min Max
#  0      12     12       12       0   0
#  1      24     12       24       0   1
#  2      10     10       24       1   1
#  3      24     10       24       1   1
# Given the scores for a season, find and 
# print the number of times Maria breaks her records 
# for most and least points scored during the season.

# Sample Input
# 9
# 10 5 20 20 4 5 2 25 1

# Sample Output
# 2 4
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


def breakingRecords(scores):
    min = max = scores[0]
    min_count = max_count = 0
    for i in scores:
        if i > max:
            max_count += 1
            max = i
        if i < min:
            min_count += 1
            min = i
    return max_count, min_count
    

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)