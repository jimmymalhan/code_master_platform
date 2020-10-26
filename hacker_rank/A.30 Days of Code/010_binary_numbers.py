# represents in 1s and 0s

# Constraints
# 1 <= n <= 10^6

# sample input
# 5
# sample output
# 1
# sample input
# 13
# sample output
# 2

n = int(input())

current_consecutive_1s = 0
max_consecutive_1s = 0
while n > 0:
    remainder = n % 2
    if remainder == 1:
        current_consecutive_1s += 1
        if current_consecutive_1s > max_consecutive_1s:
            max_consecutive_1s = current_consecutive_1s
    else:
        current_consecutive_1s = 0
    n = n // 2 # reset it to loop again by floor division "//" eg = 10 // 3 = 3

print(max_consecutive_1s)